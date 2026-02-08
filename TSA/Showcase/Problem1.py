def musical_fizzbuzz(n):
    
    result = []
    if n % 3 == 0 and n % 5 == 0:
        result.append("RockPop")
        if '7' in str(n):
            result[-1] += "Jazz"
    elif n % 3 == 0:
        result.append("Rock")
        if '7' in str(n):
            result[-1] += "Jazz"
    elif n % 5 == 0:
        result.append("Pop")
        if '7' in str(n):
            result[-1] += "Jazz"
    else:
        result.append(str(n))

    return result

if __name__ == "__main__":
    n = int(input())
    output = musical_fizzbuzz(n)
    print("\n".join(output))