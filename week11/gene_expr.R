setwd("~/Desktop")
install.packages("tidyr")
library(tidyr)
library(dplyr)
df = read.csv("cell_expr.csv",header=T)
head(df)

df_dataonly = df %>% select(gene_names, cfu, mys, unk, poly)

test = df_dataonly %>% gather(., key, ex_levels, -gene_names) %>%
	mutate(stage=ifelse(key =="cfu"| key == "mys", "early","late")) %>%
	mutate(gene = as.character(gene_names))


smalltest = test %>% filter(gene == "Car1"| gene == "Mir682")
genelist = test %>% select(gene) %>% unique(.)

ttestfn = function(genename, dataframe){
	print(genename)
	genedf = dataframe %>% filter(gene == genename)
	ans = t.test(ex_levels~stage, data = genedf)
	return(data.frame(genename,ans$p.value))
}

runtests = lapply(genelist$gene, ttestfn, dataframe = test)

results = do.call("rbind", runtests)

tryttestfn = function(genename, dataframe){
	print(genename)
	genedf = dataframe %>% filter(gene == gene_names)
	ans = try(t.test(ex_levels~stage, data = genedf), silent=TRUE)
	if (is(ans, "try-error")) return(data.frame(genename,pval = NA)) else return(data.frame(genename,pval = ans$p.value))
	
}
sig_results = results %>% filter(ans.p.value <= 0.05)

write.csv(sig_results, file = "diff_expr_genes.csv")

earlymean = df %>% group_by(gene) %>% summarise(earlymean = mean(c(CFU,mys)))

latemean = df %>% group_by(gene) %>% summarise(earlymean = mean(c(poly,runk)))

df2 = df %>% mutate(earlyMean = mean(CFU,mys)) #%>% mutate (lateMean = mean(c(poly, runk))) %>% mutate (diff= lateMean - earlyMean)
head(df2)
df2 %>% summarize(diff == max(diff))
