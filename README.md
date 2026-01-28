# Parametric Facade & Simulation Systems

A Python-based parametric design tool that generates facade patterns using curve attractors and mathematical functions, simulating the behavior of Grasshopper's attractor systems.

## 🎯 Project Overview

This project demonstrates computational design principles by creating dynamic facade systems where panel properties (rotation, scale, opacity) are controlled by attractor points. The system mimics Grasshopper's curve attractor workflow but is implemented in pure Python, making it accessible and customizable.

## ✨ Features

- **Curve Attractor System**: Define attractor points that influence surrounding panels
- **Multiple Attractor Support**: Combine multiple attractors for complex patterns
- **Parametric Control**: Adjust grid size, attractor strength, and influence radius
- **Visual Output**: Generate high-resolution facade visualizations
- **Data Export**: Export panel data as JSON for use in Revit, Rhino, or other BIM tools
- **Falloff Functions**: Realistic influence decay based on distance

## 🛠️ Technical Details

### Core Components

1. **ParametricFacade Class**: Main class for facade generation
   - Grid-based panel system
   - Attractor management
   - Influence calculation with distance-based falloff
   
2. **Panel Properties**: Each panel dynamically adjusts based on attractor influence
   - Rotation (0-45 degrees)
   - Scale (0.5-1.0)
   - Opacity (0.3-1.0)

3. **Visualization Engine**: Uses matplotlib for rendering
   - High-resolution output (300 DPI)
   - Visual representation of influence radii
   - Grid-based layout with proper scaling

### Technologies Used

- **Python 3.x**
- **NumPy**: Mathematical calculations and array operations
- **Matplotlib**: Visualization and rendering
- **JSON**: Data export for BIM integration

## 📊 Usage Examples

### Basic Usage

```python
from parametric_facade import ParametricFacade

# Create a 20m x 15m facade with 1m grid
facade = ParametricFacade(width=20, height=15, grid_size=1.0)

# Add a central attractor
facade.add_attractor(x=10, y=7.5, strength=1.0, radius=8.0)

# Generate and visualize
facade.visualize(save_path='my_facade.png')

# Export data for BIM
facade.export_data('facade_data.json')
```

### Multiple Attractors

```python
facade = ParametricFacade(width=20, height=15, grid_size=0.8)

# Add multiple attractors
facade.add_attractor(x=5, y=5, strength=0.8, radius=6.0)
facade.add_attractor(x=15, y=10, strength=0.9, radius=7.0)
facade.add_attractor(x=10, y=12, strength=0.7, radius=5.0)

facade.visualize(save_path='complex_facade.png')
```

## 🎨 Example Outputs

This repository includes three example facade designs:

1. **Single Central Attractor**: Demonstrates radial influence pattern
2. **Multiple Attractors**: Shows complex overlapping influence zones
3. **Linear Pattern**: Displays rhythmic facade variation

## 💡 Value Proposition

### Unique Value
- **Computational Design Automation**: Reduces manual facade design iterations
- **Data-Driven Design**: Mathematical control over aesthetic outcomes
- **BIM Integration Ready**: Exports data compatible with Revit and Rhino
- **Rapid Prototyping**: Generate multiple design options quickly

### Relevance
- **Aviation Projects**: Applicable to terminal facade design with performance-driven patterns
- **Large-Scale Infrastructure**: Demonstrates ability to handle complex parametric systems
- **Design-to-Fabrication**: Exportable data supports digital fabrication workflows
- **Educational Tool**: Can be used to teach parametric design concepts

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/kavyasista96/parametric-facade-systems.git

# Install dependencies
pip install numpy matplotlib

# Run the example script
python parametric_facade.py
```

## 📦 Output Files

The script generates the following files:

- **facade_single_attractor.png**: Visualization with single attractor
- **facade_multiple_attractors.png**: Visualization with multiple attractors
- **facade_linear_pattern.png**: Visualization with linear pattern
- **facade_data.json**: Panel data for BIM import

## 🚀 Future Enhancements

- [ ] Physics-based simulation (wind load, structural analysis)
- [ ] Integration with Grasshopper via GH Python components
- [ ] Real-time Revit API integration
- [ ] Environmental analysis (solar exposure, shading)
- [ ] 3D extrusion and depth variation
- [ ] Material properties and cost estimation

## 📝 Connection to Professional Work

This project bridges my background in computational design (Grasshopper, Rhino) with Python automation skills used in my BIM workflow at Abstract Group. It demonstrates the ability to:

- Translate visual programming logic to Python code
- Create reusable design tools
- Export data for BIM integration
- Apply mathematical concepts to architectural design

## 👤 Author

**Kavya Sista**
- Computational Designer & Architectural Designer
- GitHub: [@kavyasista96](https://github.com/kavyasista96)
- LinkedIn: [kavya-sista-600951154](https://linkedin.com/in/kavya-sista-600951154)

## 📄 License

MIT License - Feel free to use and modify for your projects.

---

*Built with Python, NumPy, and Matplotlib | Part of professional portfolio demonstrating computational design capabilities*
