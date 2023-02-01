verb_suffixes = {"en", "o", "os", "a", "om", "ons", "am", "ei", "es", "e", "em", "est", "im", "ai", "ais", "i", "aem", "aist", "aim"}
tempos = {"Presente", "Pretérito", "Futuro"}


conjugacao = {
    "Presente": {"1a pessoa": "o", "2a pessoa": "os", "3a pessoa": "a", "4a pessoa": "om", "5a pessoa": "ons", "6a pessoa": "am"},
    "Pretérito": {"1a pessoa": "ei", "2a pessoa": "es", "3a pessoa": "e", "4a pessoa": "em", "5a pessoa": "est", "6a pessoa": "im"},
    "Futuro": {"1a pessoa": "ai", "2a pessoa": "ais", "3a pessoa": "i", "4a pessoa": "aem", "5a pessoa": "aist", "6a pessoa": "aim"}
}

def analisar_verbo(palavra):
#corraem tá sumindo a A
    for suffix in verb_suffixes:
        if palavra.endswith(suffix):
            verbo = palavra
            suffix = 'en'
            verbo = palavra[ :-len(suffix)]
            verbo_com_sufixo = "{}{}".format(verbo, suffix)
            for tempo, pessoas in conjugacao.items():
                for pessoa, sufixo in pessoas.items():
                    if palavra.endswith(sufixo):
                        return f"{palavra} ({verbo_com_sufixo}): {pessoa} {tempo}"
            return f"{palavra} ({verbo_com_sufixo}): Verbo regular"
    else:
        return f"{palavra}: Não é verbo"

palavras = input("Insira uma lista de palavras: ").strip().split("\n")
for palavra in palavras:
    print(analisar_verbo(palavra))
