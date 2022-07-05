my_text = """in p$imava$a anu^ui 1894, t%ata ^%nd$a a f%!t int#$#!ata, ia$
^um#a ^a m%da a f%!t &%n!t#$nata d# u&id#$#a %n%$abi^u^ui $%na^d
adai$ in &i$&um!tant# &#^# mai n#%bi!nuit# !i in#xp^i&abi^#.
pub^i&u^ a af^at d#ja a&#^# d#ta^ii a^# &$im#i &a$# au i#!it ^a
iv#a^a in an&@#ta p%^iti#i; da$ mu^t# au f%!t !up$imat# &u a&#a
%&azi#, d#%a$#&# &azu^ a&uza$ii #$a atat d# &%p^#!it%$ d#
put#$ni&, in&at nu #$a n#&#!a$ !a !# p$#zint# t%at# fapt#^#. abia
a&um, ^a !fa$!itu^ a ap$%ap# z#&# ani, imi #!t# p#$mi! !a
ap$%vizi%n#z a&#^# v#$igi ^ip!a &a$# a^&atui#!& int$#gu^ ^ant
$#ma$&abi^. &$ima #$a int#$#!anta in !in#, da$ a&#^ int#$#! nu
#$a nimi& p#nt$u min# in &%mpa$ati# &u &%ntinua$#a d# n#&%n&#put,
&a$# mi-a %f#$it &#^ mai ma$# !%& !i !u$p$iza din %$i&# #v#nim#nt
din vitța m#a av#ntu$%a!a. &@ia$ !i a&um, dupa a&#!t int#$va^
^ung, mă t$#z#!& #m%ti%nat &and ma gand#!& ^a a!ta !i !imt din
n%u a&#^ p%t%p b$u!& d# bu&u$i#, uimi$# !i n#in&$#d#$# &a$# mi-a
&ufundat &u t%tu^ mint#a."""
litere = {'!': 's',
          '@': 'h',
          '#': 'e',
          '$': 'r',
          '^': 'l',
          '%': 'o',
          '&': 'c',
          '*': 'k'}
result_a = ''
for i in my_text:
    if i in litere.keys():
        result_a += litere[i]
    else:
        result_a += i

print(result_a)

print(80 * '#')
# b). with dot split
# disadvantages to using this:
# result is just printed not stored in a variable
# strip will delete multiple spaces and \n \r so that there is no way to exactly re assemble the text back correctly
# this will add an unwanted  ". " so it does not work correctly for the text given !
text_spart = result_a.split(".")
for i in text_spart:
    print(i.strip().capitalize(), end=". ")

print(80 * '#')
# b. with word split
c = False
result_b = ''
for i in result_a.split(' '):
    if c:
        i = i.capitalize()
        c = False
    if '.' in i:
        c = True
    result_b = f"{result_b} {i}"

print(result_b)

print(80 * '#')
# with distance to the applied condition more generic
# this does not work correctly with extra spaces but can be adjusted
result_b = ''
counter = 0
for i in result_a:
    if i == '.':
        counter = 3
    if counter == 1:
        i = i.upper()
        counter = 0
    else:
        counter -= 1
    result_b += i
print(result_b)

print(80 * '#')
# b. this method allows us to also check a condition in advance
# also relays on precise number of chars after .
iter_result = result_a.__iter__()
result_b = ''
for i in iter_result:
    if i == '.':
        result_b += i
        try:
            result_b += next(iter_result)  # generally the next empty space or \n after dot
            result_b += next(iter_result).upper()  # generally the next letter
        except StopIteration:  # this is required because "." is the last chart.
            break
    else:
        result_b += i
print(result_b)

print(80 * '#')

# c).
text_si_mai_spart = result_a.replace(",", "").replace(".", "").replace(";", "").split(" ")
lista = []
for i in text_si_mai_spart:
    lista.append(i)
print(lista)

print(80 * '#')
# d).
scurte = 0
medii = 0
lungi = 0
for i in text_si_mai_spart:
    if len(i) <= 5:
        scurte = scurte + 1
    if 5 < len(i) <= 8:
        medii = medii + 1
    if len(i) > 8:
        lungi = lungi + 1
print("Avem", str(scurte), "cuvinte scurte.")
print("Avem", str(medii), "cuvinte medii.")
print("Avem", str(lungi), "cuvinte lungi.")
