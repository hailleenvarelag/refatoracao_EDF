import pandas as pd
import numpy as np


class AlteracoesRegistros():
    
    def __init__(self,df):
        self.df = df
        
    def alterar_F500(self):
        self.df.loc[self.df[0] == 'F500',2] ='06'
        self.df.loc[self.df[0] == 'F500',7] ='06'
    
    def alterar_F525(self):
        self.df.loc[self.df[0] == 'F525',7] ='06'
        self.df.loc[self.df[0] == 'F525',8] ='06'
    
    def zerar_M200(self):
        self.df.loc[self.df[0] == 'M200', 1:12] = '0'

    def zerar_M600(self):
        self.df.loc[self.df[0] == 'M600', 1:12] = '0'

    def alterar_M400(self):
        self.df.loc[self.df[0] == 'M400',1] = '06'
    
    def alterar_M800(self):
        self.df.loc[self.df[0] == 'M800',1] = '06'
    
    def alterar_M410(self):
        self.df.loc[self.df[0] == 'M410',1] = '920'
    
    def alterar_M810(self):
        self.df.loc[self.df[0] == 'M810',1] = '920'
    
    def excluir_M210(self):
        self.df = self.df[self.df[0] != 'M210']
    
    def excluir_M610(self):
        self.df = self.df[self.df[0] != 'M610']

    #Arquivo não consolidados

    def alterar_A170(self):
        colunas = [10, 11, 14, 15]
        self.df.loc[self.df[0] == 'A170', colunas] = '00'
        self.df.loc[self.df[0] == 'A170', [8,12]] = '06'
    
    def alterar_C170(self):
        colunas = [10, 11, 14, 15]
        self.df.loc[self.df[0] == 'C170', colunas] = '00'
        self.df.loc[self.df[0] == 'C170', [8,12]] = '06'
        
    def alterar_A100(self):
        colunas = [15,17,18,19]
        self.df.loc[self.df[0] == 'A100', colunas] = '00'

    def alterar_C100(self):
        colunas = [15,17,18,19]
        self.df.loc[self.df[0] == 'C100', colunas] = '00'
    


        

    

    