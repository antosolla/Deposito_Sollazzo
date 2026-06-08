eta = int(input("Inserisci la tua eta"))
flag = False # creo un flag che mi indicherà al match case cosa fare

if (eta >= 18):
    flag=True #maggiorenne, spunto il flag

match flag:
    case True:
        print("Puoi vedre il film")
    case False:
        print("Mi dispace. Non puoi vedere questo film")