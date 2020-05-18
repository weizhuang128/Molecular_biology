# Deletion Primers Lite Version 1.0
# (c) August 12, 2015 by Zhuang Victor WEI, SIBCB, CAS
# Deletion Primers is a  Tool for design overlaping deletion PCR primers.
# This version of Deletion Primers is free of charge and may be distributed freely, but not sold.
# Commercial usage is allowed.
# But you are using this software at your own risk.
# For any discussion you can email zhuangwei128@gmail.com

from Tkinter import *
from Bio.Seq import Seq

root = Tk(className=' Deletion Primers')
label_Start = Label(root)
label_Start['text'] = 'Author: Zhuang WEI (wechat: zhuangsheng128)'
label_Start.pack()
label_Start = Label(root)
label_Start['text'] = '1. Enter the full length mRNA sequence'
label_Start.pack()

mRNA_text = Text(root, height=10)
mRNA_text.insert(INSERT,
                 "ATGGACAAGTTTTGGTGGCACGCAGCCTGGGGACTCTGCCTCGTGCCGCTGAGCCTGGCGCAGATCGATTTGAATATAACCTGCCGCTTTGCAGGTGTATTCCACGTGGAGAAAAATGGTCGCTACAGCATCTCTCGGACGGAGGCCGCTGACCTCTGCAAGGCTTTCAATAGCACCTTGCCCACAATGGCCCAGATGGAGAAAGCTCTGAGCATCGGATTTGAGACCTGCAGGTATGGGTTCATAGAAGGGCATGTGGTGATTCCCCGGATCCACCCCAACTCCATCTGTGCAGCAAACAACACAGGGGTGTACATCCTCACATCCAACACCTCCCAGTATGACACATATTGCTTCAATGCTTCAGCTCCACCTGAAGAAGATTGTACATCAGTCACAGACCTGCCCAATGCCTTTGATGGACCAATTACCATAACTATTGTTAACCGTGATGGCACCCGCTATGTCCAGAAAGGAGAATACAGAACGAATCCTGAAGACATCTACCCCAGCAACCCTACTGATGATGACGTGAGCAGCGGCTCCTCCAGTGAAAGGAGCAGCACTTCAGGAGGTTACATCTTTTACACCTTTTCTACTGTACACCCCATCCCAGACGAAGACAGTCCCTGGATCACCGACAGCACAGACAGAATCCCTGCTACCAGTACGTCTTCAAATACCATCTCAGCAGGCTGGGAGCCAAATGAAGAAAATGAAGATGAAAGAGACAGACACCTCAGTTTTTCTGGATCAGGCATTGATGATGATGAAGATTTTATCTCCAGCACCATTTCAACCACACCACGGGCTTTTGACCACACAAAACAGAACCAGGACTGGACCCAGTGGAACCCAAGCCATTCAAATCCGGAAGTGCTACTTCAGACAACCACAAGGATGACTGATGTAGACAGAAATGGCACCACTGCTTATGAAGGAAACTGGAACCCAGAAGCACACCCTCCCCTCATTCACCATGAGCATCATGAGGAAGAAGAGACCCCACATTCTACAAGCACAATCCAGGCAACTCCTAGTAGTACAACGGAAGAAACAGCTACCCAGAAGGAACAGTGGTTTGGCAACAGATGGCATGAGGGATATCGCCAAACACCCAGAGAAGACTCCCATTCGACAACAGGGACAGCTGCAGCCTCAGCTCATACCAGCCATCCAATGCAAGGAAGGACAACACCAAGCCCAGAGGACAGTTCCTGGACTGATTTCTTCAACCCAATCTCACACCCCATGGGACGAGGTCATCAAGCAGGAAGAAGGATGGATATGGACTCCAGTCATAGTACAACGCTTCAGCCTACTGCAAATCCAAACACAGGTTTGGTGGAAGATTTGGACAGGACAGGACCTCTTTCAATGACAACGCAGCAGAGTAATTCTCAGAGCTTCTCTACATCACATGAAGGCTTGGAAGAAGATAAAGACCATCCAACAACTTCTACTCTGACATCAAGCAATAGGAATGATGTCACAGGTGGAAGAAGAGACCCAAATCATTCTGAAGGCTCAACTACTTTACTGGAAGGTTATACCTCTCATTACCCACACACGAAGGAAAGCAGGACCTTCATCCCAGTGACCTCAGCTAAGACTGGGTCCTTTGGAGTTACTGCAGTTACTGTTGGAGATTCCAACTCTAATGTCAATCGTTCCTTATCAGGAGACCAAGACACATTCCACCCCAGTGGGGGGTCCCATACCACTCATGGATCTGAATCAGATGGACACTCACATGGGAGTCAAGAAGGTGGAGCAAACACAACCTCTGGTCCTATAAGGACACCCCAAATTCCAGAATGGCTGATCATCTTGGCATCCCTCTTGGCCTTGGCTTTGATTCTTGCAGTTTGCATTGCAGTCAACAGTCGAAGAAGGTGTGGGCAGAAGAAAAAGCTAGTGATCAACAGTGGCAATGGAGCTGTGGAGGACAGAAAGCCAAGTGGACTCAACGGAGAGGCCAGCAAGTCTCAGGAAATGGTGCATTTGGTGAACAAGGAGTCGTCAGAAACTCCAGACCAGTTTATGACAGCTGATGAGACAAGGAACCTGCAGAATGTGGACATGAAGATTGGGGTGTAA")
mRNA_text.pack()

label_Start = Label(root)
label_Start['text'] = '2. Enter the Start Position of the Protein Domain You Will be Deleted'
label_Start.pack()

text_Start = StringVar()
text_Start.set('Protein Position')

entry_Start = Entry(root)
entry_Start['textvariable'] = text_Start
entry_Start.pack()

label_End = Label(root)
label_End['text'] = '3. Enter the End Position of the Protein Domain You Will be Deleted'
label_End.pack()

text_End = StringVar()
text_End.set('Protein Position')

entry_End = Entry(root)
entry_End['textvariable'] = text_End
entry_End.pack()


def get_the_delete_primer():
    up_start = entry_Start.get()
    down_end = entry_End.get()

    target_mrna = Seq(mRNA_text.get('0.0', END))
    print(target_mrna)

    target_mrna_len = len(target_mrna)
    print "The Target mRNA Length is:", (target_mrna_len)

    print "Delete", (up_start), "-", (down_end)

    # if (up_start > 6) and (down_end > (target_mrna_len - 6))
    # Using up_start and down_end as numbers to count.

    up_primer = target_mrna[(int(up_start) * 3 - 19):(int(up_start) * 3 - 3)]
    print "The Up_primer is:", (up_primer)
    down_primer = target_mrna[(int(down_end) * 3):(int(down_end) * 3 + 16)]
    print "The Down_primer is:", (down_primer)
    # This think is because Python slicing is the start number but NOT conclude to the end number DO conclude. Therefore the end up_start is directly the mRNA sequence number, the start down_end is the mRNA number-1

    # If the entered start or end number is <=6 to both boundaries, there will be a half primer here.

    down_sense_primer = up_primer + down_primer

    up_antisense_primer = down_sense_primer.reverse_complement()

    The_Upstream_Antisense_Primer = str(up_antisense_primer)
    The_Downstream_Sense_Primer = str(down_sense_primer)
    print "The Upstream Antisense Primer is:", (The_Upstream_Antisense_Primer)
    print "The Downstream Sense Primer is:", (The_Downstream_Sense_Primer)

    label_Upstream_Antisense_Primer = Label(root)
    label_Upstream_Antisense_Primer['text'] = "The_Upstream_Antisense_Primer_for_deleting_", (up_start), "-", (down_end)
    label_Upstream_Antisense_Primer.pack()

    Upstream_Antisense_Primer = Entry(root, width=40)
    Upstream_Antisense_Primer['textvariable'] = Upstream_Antisense_Primer.insert(0, The_Upstream_Antisense_Primer)
    Upstream_Antisense_Primer.pack()

    label_Downstream_Sense_Primer = Label(root)
    label_Downstream_Sense_Primer['text'] = "The_Downstream_Sense_Primer_for_deleting_", (up_start), "-", (down_end)
    label_Downstream_Sense_Primer.pack()

    Downstream_Sense_Primer = Entry(root, width=40)
    Downstream_Sense_Primer['textvariable'] = Downstream_Sense_Primer.insert(0, The_Downstream_Sense_Primer)
    Downstream_Sense_Primer.pack()


design = Button(root, command=get_the_delete_primer)
design['text'] = 'Design'
design.pack()

root.mainloop()

