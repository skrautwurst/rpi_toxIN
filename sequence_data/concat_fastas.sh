#!/bin/bash
#concatenate multiple fastas into one large fasta

WORKDIR=/data/fass1/genomes/new_bacteria/all_bacteria

# if all files are in the same directory:
#cat "$WORKDIR"/*.fna > "$WORKDIR"/all_genomes.fna


# if files are in different subfolders:
EXT=( *.fna )

for SUBDIR in "$WORKDIR"/*/; do
  cd "$SUBDIR"
  if (( ${#EXT[@]} ))
  then
    cat *.fna >> /data/prostlocal2/projects/sk_rnaprotein/masterthesis/rpi_toxIN/all_genomes.fna
    echo "$SUBDIR fna files added to all_genomes.fna"
    # echo $(basename $SUBDIR) "fna files added to all_genomes.fna" >> output.log
  else
    echo "No fna files for directory $SUBDIR available!"
    # echo "No fna files for directory" $(basename $SUBDIR) "available!" >> output.log
  fi
done

