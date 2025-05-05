def celsius(celsius2):
    
    faherenheit = (celsius2 * 9/5) + 32
    
    return faherenheit
    
def faherenheit(faherenheit2):
    
    celsius = (faherenheit2 - 32)*5/9
    
    return celsius

opcao = int(input("digite um 1-pra transforma celsius para fahrenheit" \
" 2- pra tansformar fahrenheit para celsius "))

if opcao == 1:
    c = float(input("digite a temperatura: "))
    f =celsius(c)
    print(f"{c}C equivale a {f:.2f}F")

elif opcao== 2:
    f = float(input("digite a temperatura"))
    c = faherenheit(f)
    print(f"{f}C equivale a {c:.2f} ")