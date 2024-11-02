year = int(input("Enter a year: "))

if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leap year")
elif (year % 4 == 0) and (year %100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

'''Basic Rule: Most years that are divisible by 4 are leap years.
Correction Rule: However, every 100 years, we need to skip a leap year to correct for the overage.
Exception Rule: But every 400 years, we go back to counting that year as a leap year.

conclusion: divisible by-
400 and 100
4 and NOT 100'''


