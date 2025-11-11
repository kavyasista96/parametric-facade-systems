"""
Parametric Facade Generator
Author: Kavya Sista
Description: Generates parametric facade patterns using curve attractors and mathematical functions
             Simulates the behavior of Grasshopper's curve attractor systems in Python
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from matplotlib.collections import PatchCollection
import json

class ParametricFacade:
    """
    A class to generate parametric facade systems with attractor-based panel variations
    """
    
    def __init__(self, width=20, height=15, grid_size=1.0):
        """
        Initialize the facade grid
        
        Parameters:
        - width: Width of the facade in meters
        - height: Height of the facade in meters
        - grid_size: Size of each panel grid cell
        """
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.grid_x = int(width / grid_size)
        self.grid_y = int(height / grid_size)
        self.attractors = []
        
    def add_attractor(self, x, y, strength=1.0, radius=10.0):
        """
        Add an attractor point that influences panel properties
        
        Parameters:
        - x, y: Position of the attractor
        - strength: Influence strength (0-1)
        - radius: Maximum influence radius
        """
        self.attractors.append({
            'position': (x, y),
            'strength': strength,
            'radius': radius
        })
    
    def calculate_influence(self, x, y):
        """
        Calculate the cumulative influence of all attractors at a given point
        """
        total_influence = 0
        
        for attractor in self.attractors:
            ax, ay = attractor['position']
            distance = np.sqrt((x - ax)**2 + (y - ay)**2)
            
            if distance < attractor['radius']:
                # Falloff function: influence decreases with distance
                influence = attractor['strength'] * (1 - distance / attractor['radius'])
                total_influence += influence
        
        return min(total_influence, 1.0)  # Cap at 1.0
    
    def generate_panels(self):
        """
        Generate facade panels with properties based on attractor influence
        Returns array of panel data
        """
        panels = []
        
        for i in range(self.grid_x):
            for j in range(self.grid_y):
                # Center position of the panel
                x = i * self.grid_size + self.grid_size / 2
                y = j * self.grid_size + self.grid_size / 2
                
                # Calculate influence at this position
                influence = self.calculate_influence(x, y)
                
                # Panel properties vary based on influence
                panel = {
                    'position': (i * self.grid_size, j * self.grid_size),
                    'size': self.grid_size,
                    'rotation': influence * 45,  # Rotate up to 45 degrees
                    'scale': 0.5 + (influence * 0.5),  # Scale from 0.5 to 1.0
                    'opacity': 0.3 + (influence * 0.7),  # Opacity from 0.3 to 1.0
                    'influence': influence
                }
                
                panels.append(panel)
        
        return panels
    
    def visualize(self, show_attractors=True, save_path=None):
        """
        Visualize the parametric facade
        """
        panels = self.generate_panels()
        
        fig, ax = plt.subplots(figsize=(12, 9))
        
        # Draw panels
        for panel in panels:
            x, y = panel['position']
            size = panel['size'] * panel['scale']
            rotation = panel['rotation']
            opacity = panel['opacity']
            
            # Create rectangle for panel
            offset = (self.grid_size - size) / 2
            rect = Rectangle(
                (x + offset, y + offset),
                size,
                size,
                angle=rotation,
                facecolor='steelblue',
                edgecolor='white',
                alpha=opacity,
                linewidth=0.5
            )
            ax.add_patch(rect)
        
        # Draw attractors if enabled
        if show_attractors and self.attractors:
            for attractor in self.attractors:
                att_x, att_y = attractor['position']
                radius = attractor['radius']
                
                # Draw influence radius
                circle = Circle(
                    (att_x, att_y),
                    radius,
                    fill=False,
                    edgecolor='red',
                    linestyle='--',
                    linewidth=1.5,
                    alpha=0.5
                )
                ax.add_patch(circle)
                
                # Draw attractor point
                ax.plot(att_x, att_y, 'ro', markersize=10, markeredgecolor='darkred', markeredgewidth=2)
        
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.set_aspect('equal')
        ax.set_facecolor('#f0f0f0')
        ax.set_title('Parametric Facade System with Curve Attractors', 
                     fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Width (m)', fontsize=12)
        ax.set_ylabel('Height (m)', fontsize=12)
        ax.grid(True, alpha=0.2)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Facade visualization saved to: {save_path}")
        
        plt.show()
    
    def export_data(self, filename='facade_data.json'):
        """
        Export panel data for use in other applications (Revit, Rhino, etc.)
        """
        panels = self.generate_panels()
        
        export_data = {
            'metadata': {
                'width': self.width,
                'height': self.height,
                'grid_size': self.grid_size,
                'total_panels': len(panels)
            },
            'attractors': self.attractors,
            'panels': panels
        }
        
        with open(filename, 'w') as f:
            json.dump(export_data, f, indent=2)
        
        print(f"Panel data exported to: {filename}")
        return filename


def create_example_facades():
    """
    Create several example facade designs
    """
    
    print("Generating Parametric Facade Examples...")
    print("=" * 60)
    
    # Example 1: Single Central Attractor
    print("\n1. Creating facade with single central attractor...")
    facade1 = ParametricFacade(width=20, height=15, grid_size=1.0)
    facade1.add_attractor(x=10, y=7.5, strength=1.0, radius=8.0)
    facade1.visualize(save_path='facade_single_attractor.png')
    
    # Example 2: Multiple Attractors
    print("\n2. Creating facade with multiple attractors...")
    facade2 = ParametricFacade(width=20, height=15, grid_size=0.8)
    facade2.add_attractor(x=5, y=5, strength=0.8, radius=6.0)
    facade2.add_attractor(x=15, y=10, strength=0.9, radius=7.0)
    facade2.add_attractor(x=10, y=12, strength=0.7, radius=5.0)
    facade2.visualize(save_path='facade_multiple_attractors.png')
    
    # Example 3: Linear Attractor Pattern
    print("\n3. Creating facade with linear attractor pattern...")
    facade3 = ParametricFacade(width=20, height=15, grid_size=0.7)
    for i in range(4):
        facade3.add_attractor(x=5 + i*5, y=7.5, strength=0.8, radius=4.0)
    facade3.visualize(save_path='facade_linear_pattern.png')
    
    # Export data for the first example
    facade1.export_data('facade_data.json')
    
    print("\n" + "=" * 60)
    print("✓ All facade examples generated successfully!")
    print("\nGenerated files:")
    print("  - facade_single_attractor.png")
    print("  - facade_multiple_attractors.png")
    print("  - facade_linear_pattern.png")
    print("  - facade_data.json (panel data for Revit/Rhino import)")


if __name__ == "__main__":
    create_example_facades()
