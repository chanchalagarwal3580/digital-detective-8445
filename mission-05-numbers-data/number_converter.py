#!/usr/bin/env python3
"""
Digital Detective - Mission 5: Number Converter
Author: Chanchal Agarwal
Description: Converts user-entered decimal integers into binary and hexadecimal representations,
handling invalid inputs gracefully.
"""

def convert_number():
    print("=" * 45)
    print("      DIGITAL DETECTIVE NUMBER CONVERTER     ")
    print("=" * 45)
    
    while True:
        user_input = input("\nEnter a positive decimal integer (or 'q' to quit): ").strip()
        
        if user_input.lower() == 'q':
            print("Exiting Number Converter. Goodbye!")
            break
            
        try:
            # Parse user input into an integer
            decimal_value = int(user_input)
            
            if decimal_value < 0:
                print("Error: Please enter a positive integer (0 or greater).")
                continue
                
            # Perform conversions using Python built-in functions
            binary_representation = bin(decimal_value)
            hex_representation = hex(decimal_value)
            
            # Format outputs cleanly
            print(f"\n--- Conversion Results for Decimal {decimal_value} ---")
            print(f"  Decimal (Base 10)     : {decimal_value}")
            print(f"  Binary (Base 2)       : {binary_representation} (Raw: {binary_representation[2:]})")
            print(f"  Hexadecimal (Base 16) : {hex_representation} (Raw: {hex_representation[2:].upper()})")
            
        except ValueError:
            print(f"Invalid input: '{user_input}'. Please enter a valid decimal number.")

if __name__ == "__main__":
    convert_number()
