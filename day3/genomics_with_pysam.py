import sys

import pysam


def pysam_read_sam_file():
    samfile = pysam.AlignmentFile("/home/alanah/SRR20334685.sam", "r")
    count = 0
    for read in samfile:
        if count > 10: #only count first ten, for each read in sam file (prints one at a time) show me this read, read is an object of type alignsegement
            break
        print(f"{read = }")  # https://pysam.readthedocs.io/en/latest/api.html#pysam.AlignedSegment
        count += 1
        # print(f"{read.bin = }")
        # print(f"{read.cigarstring = }")
        # print(f"{read.get_aligned_pairs() = }")
    samfile.close()


def pysam_read_bam_file():
    with pysam.AlignmentFile("/home/alanah/SRR20334685.final.bam") as bamfile:
        # fetch by region
        for read in bamfile.fetch("I", 1000, 2000):    ##looking for a specfic region (genomic coordinates)
            print(f"{read = }")  # https://pysam.readthedocs.io/en/latest/api.html#pysam.AlignedSegment
            print(f"{read.get_forward_sequence() = }")
            print(f"{len(read.get_forward_sequence())}")
            print(f"{read.get_forward_qualities() = }")
            print(f"{read.get_reference_positions() = }")


def pysam_get_pileup():
    with pysam.AlignmentFile("/home/alanah/SRR20334685.final.bam") as bamfile:
        # reads associated with positions
        for pileup_column in bamfile.pileup("I", 1750, 1751):
            # print(f"{pileup_column = }") # https://pysam.readthedocs.io/en/latest/api.html#pysam.PileupColumn
            print(f"{pileup_column.get_num_aligned() = }")
            print(f"{pileup_column.get_query_sequences() = }")
            print(f"{pileup_column.get_query_positions() = }")
            print(f"{pileup_column.get_query_qualities() = }")


def htseq_read_fastq():
    import HTSeq
    import itertools
    with HTSeq.FastqReader("/home/alanah/SRR20334685.fastq") as fastq_file:
        for read in itertools.islice(fastq_file, 10):
            print(f"{read = }") # https://htseq.readthedocs.io/en/master/refoverview.html
            print(f"{read.qual = }")

def main():
    # pysam_read_sam_file()
    # pysam_read_bam_file()
    # pysam_get_pileup()
    htseq_read_fastq()
    return 0


if __name__ == '__main__':
    sys.exit(main())
