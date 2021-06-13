library(UpSetR)
setwd("~/rpi_toxIN/species_comparison")

#read data
data <- read.table(file="inputfile_taxids.txt", sep="", header=TRUE)

#convert to matrix
processed <- data.frame(unclass(t(table(data$method, data$taxid))))
#input <- as.matrix(processed)

#plot
plot <- upset(processed, 
      nintersects = NA, #plot all intersections
      nsets = 15, # sets are the different databases and searching approaches
      order.by = "degree", 
      decreasing = T, 
      keep.order = T,
      sets = c("hmmsearch_hyppr", "hmmsearch_taIII", "pfam", "cmsearch_rfamlit1_mid", "cmsearch_lit1_mid", "cmsearch_lit1", "lit1", "cmsearch_rfam", "rfam", "cmsearch_pdb", "pdb"),
      mb.ratio = c(0.6, 0.4),
      text.scale = 1.1, 
      point.size = 2.8, 
      line.size = 1,
      set_size.show = TRUE,
)

plot

