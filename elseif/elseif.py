def isWeird(n):
    if n % 2 == 0 and 6 <= n <= 20:
        return "Weird"

    if n % 2 == 0:
        return "Not Weird"
    
    return "Weird"
