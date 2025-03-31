def water_column_height(tower_height, tank_height):
    """
    Calculate the height of a water column based on tower and tank dimensions.
    
    Args:
        tower_height: Height of the tower in meters
        tank_height: Height of the tank walls in meters
    
    Returns:
        Height of the water column in meters
    """
    return tower_height + (3 * tank_height) / 4

def pressure_gain_from_water_height(height):
    """
    Calculate pressure caused by Earth's gravity on a water column.
    
    Args:
        height: Height of the water column in meters
    
    Returns:
        Pressure in kilopascals (kPa)
    """
    density = 998.2  # kg/m^3
    gravity = 9.80665  # m/s^2
    return (density * gravity * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    Calculate water pressure lost due to pipe friction.
    
    Args:
        pipe_diameter: Diameter of the pipe in meters
        pipe_length: Length of the pipe in meters
        friction_factor: Pipe's friction factor (dimensionless)
        fluid_velocity: Velocity of water in meters/second
    
    Returns:
        Pressure loss in kilopascals (kPa)
    """
    density = 998.2  # kg/m^3
    numerator = -friction_factor * pipe_length * density * fluid_velocity**2
    denominator = 2000 * pipe_diameter
    return numerator / denominator

# Constants
EARTH_ACCELERATION_OF_GRAVITY = 9.80665  # m/s^2
WATER_DENSITY = 998.2  # kg/m^3
WATER_DYNAMIC_VISCOSITY = 0.0010016  # Pascal seconds

def water_column_height(tower_height, tank_height):
    return tower_height + (3 * tank_height) / 4

def pressure_gain_from_water_height(height):
    return (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    numerator = -friction_factor * pipe_length * WATER_DENSITY * fluid_velocity**2
    denominator = 2000 * pipe_diameter
    return numerator / denominator

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    return (-0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings) / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    # Calculate k constant
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter)**4 - 1)
    
    # Calculate pressure loss
    pressure_loss = (-k * WATER_DENSITY * fluid_velocity**2) / 2000
    
    return pressure_loss

def kpa_to_psi(pressure_kpa):
    return pressure_kpa * 0.145038

# Pipe specification constants
PVC_SCHED80_INNER_DIAMETER = 0.28687  # meters
PVC_SCHED80_FRICTION_FACTOR = 0.013  # unitless
SUPPLY_VELOCITY = 1.65  # meters/second
HDPE_SDR11_INNER_DIAMETER = 0.048692  # meters
HDPE_SDR11_FRICTION_FACTOR = 0.018  # unitless
HOUSEHOLD_VELOCITY = 1.75  # meters/second

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    
    # Pressure loss in supply pipe
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    
    pressure += pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    
    # Pressure loss in household pipe
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    pressure += pressure_loss_from_pipe(diameter, length2, friction, velocity)
    
    # Display results
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {kpa_to_psi(pressure):.1f} psi")

if __name__ == "__main__":
    main()