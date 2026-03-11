#!/usr/bin/env python3
"""
SPN 5464 Battery Charge Calculator
Interactive tool to calculate Hybrid Battery Pack Remaining Charge

Usage: python3 calculate_spn5464.py
"""

def calculate_battery_charge(byte0_hex, byte1_hex):
    """
    Calculate battery charge percentage from two hex bytes.
    
    Args:
        byte0_hex: First byte in hexadecimal (e.g., '40')
        byte1_hex: Second byte in hexadecimal (e.g., '9C')
    
    Returns:
        Battery charge percentage or 'Not Available'
    """
    # Convert hex to decimal
    byte0 = int(byte0_hex, 16)
    byte1 = int(byte1_hex, 16)
    
    # Combine bytes (little-endian: byte0 is LSB, byte1 is MSB)
    raw_value = byte0 + (byte1 * 256)
    
    # Check for "Not Available" sentinel value
    if raw_value == 0xFFFF:  # 65535
        return "Not Available"
    
    # Apply resolution: 0.0025% per bit
    battery_percentage = raw_value * 0.0025
    
    return battery_percentage


def print_calculation_steps(byte0_hex, byte1_hex):
    """Print detailed calculation steps."""
    print("\n" + "="*60)
    print("SPN 5464 - Battery Charge Calculation")
    print("="*60)
    
    # Step 1
    print(f"\nStep 1: Input Data")
    print(f"  Byte 0: {byte0_hex}")
    print(f"  Byte 1: {byte1_hex}")
    
    # Step 2
    byte0 = int(byte0_hex, 16)
    byte1 = int(byte1_hex, 16)
    print(f"\nStep 2: Convert Hex to Decimal")
    print(f"  Byte 0: 0x{byte0_hex} = {byte0}")
    print(f"  Byte 1: 0x{byte1_hex} = {byte1}")
    
    # Step 3
    raw_value = byte0 + (byte1 * 256)
    print(f"\nStep 3: Combine Bytes (Little-Endian)")
    print(f"  Formula: Byte₀ + (Byte₁ × 256)")
    print(f"  Calculation: {byte0} + ({byte1} × 256)")
    print(f"  Raw Value: {raw_value}")
    print(f"  Hex Combined: 0x{raw_value:04X}")
    
    # Step 4
    print(f"\nStep 4: Apply Resolution")
    if raw_value == 0xFFFF:
        print(f"  Special Case: 0xFFFF = Not Available")
        print(f"  Result: Data Not Available")
    else:
        battery_pct = raw_value * 0.0025
        print(f"  Formula: Raw Value × 0.0025")
        print(f"  Calculation: {raw_value} × 0.0025")
        print(f"  Result: {battery_pct:.2f}%")
    
    print("\n" + "="*60 + "\n")


def parse_can_message(can_data):
    """
    Parse a CAN message and extract SPN 5464 data.
    
    Args:
        can_data: CAN data string like "40 9C FF FF FF FF FF FF"
    
    Returns:
        Tuple of (byte0_hex, byte1_hex)
    """
    # Remove extra spaces and split
    bytes_list = can_data.strip().split()
    
    if len(bytes_list) < 2:
        raise ValueError("Need at least 2 bytes for SPN 5464")
    
    return bytes_list[0], bytes_list[1]


def main():
    """Main interactive calculator."""
    print("╔════════════════════════════════════════════════════════════╗")
    print("║     SPN 5464 Battery Charge Calculator                    ║")
    print("║     Hybrid Battery Pack Remaining Charge                  ║")
    print("╚════════════════════════════════════════════════════════════╝")
    
    print("\nThis tool calculates battery charge from CAN data.")
    print("You can enter data in two ways:")
    print("  1. Full CAN message: '40 9C FF FF FF FF FF FF'")
    print("  2. Just two bytes: '40 9C'")
    print("\nType 'examples' to see sample calculations")
    print("Type 'quit' to exit\n")
    
    # Pre-defined examples
    examples = [
        ("40 9C", "Full Charge (100%)"),
        ("B0 9A", "Nearly Full (99%)"),
        ("20 4E", "Half Charge (50%)"),
        ("88 13", "Low Charge (12.5%)"),
        ("FF FF", "Data Not Available"),
    ]
    
    while True:
        user_input = input("Enter CAN data bytes: ").strip()
        
        if not user_input:
            continue
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\nThank you for using the calculator!")
            break
        
        if user_input.lower() == 'examples':
            print("\n" + "="*60)
            print("Example Calculations:")
            print("="*60)
            for data, description in examples:
                byte0, byte1 = data.split()
                result = calculate_battery_charge(byte0, byte1)
                if isinstance(result, str):
                    print(f"  {data:20} → {result:>15} ({description})")
                else:
                    print(f"  {data:20} → {result:>14.2f}% ({description})")
            print("="*60 + "\n")
            continue
        
        try:
            # Parse input
            byte0, byte1 = parse_can_message(user_input)
            
            # Calculate and display
            print_calculation_steps(byte0, byte1)
            
            # Show result
            result = calculate_battery_charge(byte0, byte1)
            if isinstance(result, str):
                print(f"🔋 Battery Charge: {result}")
            else:
                print(f"🔋 Battery Charge: {result:.2f}%")
                
                # Add visual bar
                if result <= 100:
                    filled = int(result / 2)
                    bar = "█" * filled + "░" * (50 - filled)
                    print(f"   [{bar}] {result:.1f}%")
            
            print()
            
        except ValueError as e:
            print(f"❌ Error: {e}")
            print("Please enter hex bytes separated by spaces (e.g., '40 9C')\n")
        except Exception as e:
            print(f"❌ Unexpected error: {e}\n")


if __name__ == "__main__":
    main()
