def longest_unique_substring(s):
    """ Retorna o tamanho da maior substring com caracteres distintos usando Janela Deslizante (O(N)) """
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

        # Se já atingimos o máximo de 20 caracteres distintos, podemos parar
        if max_length == 20:
            return max_length

    return max_length

def max_distinct_substring(s):
    """ Maximiza a substring com caracteres distintos após inverter no máximo um trecho (O(N^2) otimizado) """
    n = len(s)

    max_len = longest_unique_substring(s)

    if max_len == 20:
        return max_len

    for i in range(n):
        for j in range(i + 1, n): 
            new_s = s[:i] + s[i:j+1][::-1] + s[j+1:]

            new_max = longest_unique_substring(new_s)

            max_len = max(max_len, new_max)

            if max_len == 20:
                return max_len

    return max_len

s = input().strip()

print(max_distinct_substring(s))