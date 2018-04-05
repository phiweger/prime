- Q5
- LongAmp


tm module for eg gotaq or custom polymerases (like initially planned for longamp) -- NEB does not reveal all buffer components (see q5) and we are thus forced to use their calculator for accurate Tm estimates and all recommendations (seems quite empirical at times)



mask

basically, w/ primers like head96f.something, head96f needs to be in sequence database, or in a mask database so we don't muddy the primer inventory, barcodes go there too

"components.csv"

then simply search for exact match and discard from what is sent to NEB -- w/ prime gather, the masked sequence is added and the comment expanded that "head96f has been masked from Tm caluclations and derived information"

---


Hi Adrian,

I think it will be nice to have following functions in our customized primer tool:

1. we should be able to upload primers in pair in csv or xlsx formats
2. we should be able to specify which enzyme we want to use
3. based on buffers used for specific enzyme the program should tell us 

Tm, annealing and extension tempertures.




4. when we enter big primer (head+primer/BC+head), we should be able to specify that 1st 16-20bases are heads or barcodes, thus the output should tell us 2 temperatures one for short primer and other for complete primer.

5. the should should except nucleotide symbols like U, R, Y, K,...and calculate Tm considering the primer is mix of 3 nucleotides.

6. Depending on the enzyme choice, it would be good to know, if we should prefer 3step or 2 step PCR, if 3 step PCR then what should be annealing and extension temperatures and if it is modified PCR (touch up which we are doing on my suggestion), then what shall be conditions for both PCR, i.e. will it be good to do 3step first and then move to 2 step with higher temperature or we can do 2 step PCR for both condition.

7. it should display warning when Tm is higher than optimal extension temperature for specific enzyme.

Now I am getting a bit more demanding but some extra suggestion which if can be incorporated in the tool will be nice;

8. depending on enzyme we should also get optimal extension time if we enter size of expected amplicon. for eg 2kb amplicon with gotaq is 2minutes but with Q5 is 1minute and longAmp is 1:40minutes. and final extension temperatures are also different for every enzyme.

9. also Program should consider enzymes from different vendors.

10. if we can enter the ncbi/Genbank id of genome or gene then it would would be nice if we can get specific conditions for PCR considering the GC content of the amplicon.

11. if it can give us some possibilities unspecific products based on unspecific binding of primers along the genome as often Tm is higher than extension temperatures.

12. we should be able to sort the list based on samples/PCR conditions/primer sets.

Thank you for thinking about the tool, it will make our life much easier.

Regards
Akash

---

3 step pcr

Normal Pcr has 3 steps:
1. Annealing: it is lower temperature step at which primers anneal to the DNA template. Normally primers are 17-23 bases and their annealing is in range of 45-60’C, i.e. 2-3 degrees lower than Tm.
2. Elongation: the best efficiency for taq is normally at a little higher temperatures like 65-72’C depending on polymerase, thus DNA synthesis on the annealed primers takes place at this step.
3. Denaturation: once DNA strand is complete we Denature the Double strand to single strand so that primers can anneal again to make more copies. This step is 94’C.
Difference of two approaches:
When we have primers which anneal at higher temperatures similar to elongation step, then we skip annealing step as we assume that after denaturation step once strands are separated primers will anneal with them as soon as temperatures falls back in range, thus we start with elongation step again. Thus is now 2 step pcr.

---

ganz so gleich sind die settings gar nicht:
Q5:
denaturation: 98°C
annealing: 64°c
extension:72°C
LongAmp:
denaturation: 94°C
annealing: 57°c
extension:64°C
GoTaq:
denaturation: 95°C
annealing: 57°c
extension:72°C

---

ein programm dafür wäre natürlich sehr hilfreich

was es bräuchte:

input:

primer name, sequenz (damit verbunden ja auch die länge des primers), polymerase (inclusive  geschwindigkeit, wie 50s/kb, temp.-range für denaturation, annealing etc.-siehe oben)

 
output:
Tm-daraus abgeleitet annealing temp. -das ist eigentlich das wichtigste
extension time (eigentlich alle temp. und zeiten, wenn das geht-)
aber ich denke, das wir da nochmal ein bisschen genauer überlegen müssen, wie das machbar wäre-errechnen der tm dauert sehr lang-dann haben wir versucht irgendwie eine gemeinsame annealing t für alle primer zu bestimmen, wobei man hier ein bisschen kompromissbereit sein muss.
der rest lässt sich ja dann aus den standard-bedingungen der polymerasen erkennen.
für 3-step PCR verhält sich das dann nochmal anders-ich denke das sollten wir mal in einer ruhighen minute genauer durchspielen...aber ja-das wäre toll.
hiermit habe ich hoffentlihc schoneinmal ein mail beantwortet;)