#!/usr/bin/env python3
# Password Strength Checker
# This script checks if a password is strong or weak

# ============================================
# VARIABLE DECLARATION
# ============================================
print("=" * 50)
print("PASSWORD STRENGTH CHECKER")
print("=" * 50)
print("Keep trying until you create a STRONG password!\n")

# Create a list of special characters to check
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']

# Variable to control the loop
password_is_strong = False

# ============================================
# MAIN LOOP - Keeps running until strong password found
# ============================================
while password_is_strong == False:
    
    # Initialize variables to track password strength criteria
    has_uppercase = False
    has_lowercase = False
    has_number = False
    has_special = False
    strength_score = 0
    number_count = 0  # Count how many numbers in password
    
    # ============================================
    # TERMINAL INPUT OF DATA
    # ============================================
    # Get password from user
    password = input("Enter your password to check its strength: ")

    # ============================================
    # CHECK FOR SPACES - Password must be one string
    # ============================================
    if ' ' in password:
        print("\n❌ NO SPACES ALLOWED! Password must be one continuous string.")
        print("Please try again without spaces.")
        print("=" * 50)
        print()
        continue  # Skip to next loop iteration

    # Variable for password length
    password_length = len(password)
    
    print("\nAnalyzing your password...")
    print("-" * 50)
    
    # ============================================
    # LOOPS - Check each character in the password
    # ============================================
    # Loop through each character in the password
    for character in password:
        
        # CASTING - Convert character to check if it's a number
        # We use try/except to safely check if it can be cast to int
        try:
            digit = int(character)  # CAST and STORE the result
            has_number = True
            number_count += 1  # Count how many numbers we found
        except ValueError:
            pass  # If it fails, it's not a number
        
        # Check if character is uppercase
        if character.isupper():
            has_uppercase = True
        
        # Check if character is lowercase
        if character.islower():
            has_lowercase = True
        
        # Check if character is a special character (using LIST)
        if character in special_characters:
            has_special = True
    
    # ============================================
    # FLOW STATEMENTS - Calculate strength score
    # ============================================
    # Check password length and add to score
    if password_length >= 8:
        strength_score += 1
        print("✓ Password is at least 8 characters long")
    else:
        print("✗ Password should be at least 8 characters long")
    
    # Check for uppercase letters
    if has_uppercase:
        strength_score += 1
        print("✓ Password contains uppercase letters")
    else:
        print("✗ Password should contain uppercase letters")
    
    # Check for lowercase letters
    if has_lowercase:
        strength_score += 1
        print("✓ Password contains lowercase letters")
    else:
        print("✗ Password should contain lowercase letters")
    
    # Check for numbers
    if has_number:
        strength_score += 1
        # CASTING: Convert integer to string for display
        count_text = str(number_count)  # Cast integer to string
        print("✓ Password contains numbers (Found " + count_text + " numbers)")
    else:
        print("✗ Password should contain numbers")
    
    # Check for special characters
    if has_special:
        strength_score += 1
        print("✓ Password contains special characters")
    else:
        print("✗ Password should contain special characters")
    
    # ============================================
    # FLOW STATEMENTS - Determine final rating
    # ============================================
    print("-" * 50)
    print(f"\nPassword Strength Score: {strength_score}/5")
    
    # Use if/elif/else to give final rating
    if strength_score == 5:
        rating = "VERY STRONG"
        print(f"Rating: {rating} 💪")
        print("Excellent! Your password is very secure.")
        password_is_strong = True  # Exit the loop!
    elif strength_score >= 4:
        rating = "STRONG"
        print(f"Rating: {rating} 👍")
        print("Good! Your password is strong, but try for VERY STRONG!")
    elif strength_score >= 3:
        rating = "MODERATE"
        print(f"Rating: {rating} 👌")
        print("Fair. Try again to make it stronger!")
    elif strength_score >= 2:
        rating = "WEAK"
        print(f"Rating: {rating} ⚠️")
        print("Warning! Try again with a stronger password.")
    else:
        rating = "VERY WEAK"
        print(f"Rating: {rating} ❌")
        print("Danger! Try again with a much stronger password.")
    
    print("=" * 50)
    print()  # Add blank line between attempts

# ============================================
# VICTORY MESSAGE - When strong password found!
# ============================================
print("\n" + "🎉" * 25)
print("YAHOO!! YOUR PASSWORD IS UNBEATABLE!!")
print("🎉" * 25)
print("\nYou successfully created a strong password!")
print("=" * 50)


# ✓ Terminal input of data: line 35 (input function)
# ✓ Variable declaration: lines 14, 17, 24-28, 37 (lists, booleans, integers)
# ✓ Loops: lines 22-119 (while loop with continue), lines 55-73 (for loop)
# ✓ Lists: line 14 (special_characters list)
# ✓ Casting: lines 61-62 (int(character) - string to integer), line 98 (str(number_count) - integer to string)
# ✓ Flow statements: lines 44-47 (if with continue), lines 81-117 (if/elif/else)
# ✓ Rudimentary terminal interface: lines 9-12, 40, 120-125

