Mwas = 22
Mary = 25

def calculate_age_difference():
    age_difference = Mary - Mwas
    return age_difference

print("Age difference between Mary and Mwas:", calculate_age_difference())

Doreen = 19

if Mwas > Mary and Doreen < Mwas:
    print("Mwas is older than Mary and Doreen is younger than Mwas, so he will marry both.")
elif Mwas < Mary and Doreen > Mwas:
    print("Mwas is younger than Mary and Doreen is older than Mwas, so he will marry Mary.")
else:
    print("He will marry Doreen.")

