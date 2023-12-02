import random
import string

def generate_random_arabic_name():
    # Arabic characters set
    arabic_chars = "ابتثجحخدذرزسشصضطظعغفقكلمنهوي"

    # Generate a random Arabic name
    name_length = random.randint(3, 10)  # Adjust the name length as needed
    random_name = ''.join(random.choice(arabic_chars) for _ in range(name_length))
    
    return random_name

def generate_random_name(length=8):
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(length))

def generate_random_7_digits():
    return ''.join(random.choice('0123456789') for _ in range(7))

def create_vcf(n, file_name):
    #UAE prefix
    prefixes = ["+97156", "+97154", "+97152", "+97150", "+97158"]
    numbers_set = set()
    
    with open(file_name, 'w') as f:
        for i in range(n):
            prefix = prefixes[i % len(prefixes)]
            unique_digits = generate_random_7_digits()
            phone_number = f"{prefix}{unique_digits}"
            
            # Ensure the generated number is unique
            while phone_number in numbers_set:
                unique_digits = generate_random_7_digits()
                phone_number = f"{prefix}{unique_digits}"
            
            numbers_set.add(phone_number)
            
            # random_name = generate_random_name()
            random_name = generate_random_arabic_name()
            
            f.write(f"""BEGIN:VCARD
VERSION:3.0
N:; {random_name} ;;;
FN: {random_name}
TEL;TYPE=CELL:{phone_number}
END:VCARD
""")
#Set the number of contacts here 
create_vcf(1000, 'contacts.vcf')
