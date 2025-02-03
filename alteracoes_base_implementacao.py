from alteracoes_base import AlteracoesBase
import pandas as pd


class ImplementandoAlteracoesBase(AlteracoesBase):
    def dados_willian(self):
        
        self.df.loc[self.df[0] == '0000', 1] = '006'
        self.df.loc[self.df[0] == '0000', 2] = '1'
        #Falta modificar o campo 4


        self.df.loc[self.df[0] == '0100', 1] = 'WILLIAM SILVA DE ALMEIDA'
        self.df.loc[self.df[0] == '0100', 2] = '89709861115'
        self.df.loc[self.df[0] == '0100', 3] = '19342DF'
        self.df.loc[self.df[0] == '0100', 6] = 'Q CRS 502 BLOCO B'
        self.df.loc[self.df[0] == '0100', 5] = '70330520'
        self.df.loc[self.df[0] == '0100', 9] = 'ASA SUL'
        self.df.loc[self.df[0] == '0100', 10] = '6181272930'
        self.df.loc[self.df[0] == '0100', 12] = 'NEGOCIOS@TAXALL.COM.BR'
        self.df.loc[self.df[0] == '0100', 13] = '5300108' 

    def calculando_contadores_de_linhas(self):
    # Contar quantas vezes '9900' aparece
        contagem_99_00 = self.df.loc[self.df[0] == '9900', 0].value_counts()

        # Encontrar os índices das linhas '9001' e '9999'
        start_index = self.df.index[self.df[0].str.startswith('9001')].min()
        end_index = self.df.index[self.df[0].str.startswith('9999')].max()

        # Criar um subconjunto do DataFrame entre '9001' e '9999'
        subset_df = self.df.loc[start_index:end_index]

        # Contar o número de linhas no subset
        contagem_linhas_99_90 = len(subset_df)

        # Calcular total de linhas -1
        contagem_total_linhas = len(self.df) - 1

        # Atualizar valores em '9999'
        self.df.loc[self.df[0] == '9999', 1] = contagem_total_linhas

        # Atualizar contagem dentro de '9900'
        self.df.loc[(self.df[0] == '9900') & (self.df[1] == '9900'), 2] = contagem_99_00.values[0]

        # Atualizar contagem de linhas para '9990'
        self.df.loc[self.df[0] == '9990', 1] = contagem_linhas_99_90

        # Excluir M210 e M610 da contagem de 'M'
        contador_M = self.df[(self.df[0].str.startswith('M')) & (~self.df[0].isin(['M210', 'M610']))].shape[0]

        # Contar as linhas que começam com 'F'
        contador_F = self.df[self.df[0].str.startswith('F')].shape[0]

        # Exibir logs no console
        print('---------- LOG Contador de linhas para Rubrica M (excluindo M210 e M610) => ', contador_M)
        print('---------- LOG Contador de linhas para Rubrica F => ', contador_F)

        # Atualizar contagem em M990 e F990
        self.df.loc[self.df[0] == 'M990', 1] = contador_M
        self.df.loc[self.df[0] == 'F990', 1] = contador_F

        # Atualizar corretamente '9900' removendo M210 e M610
        for rubrica in ['M210', 'M610']:
            self.df = self.df[~((self.df[0] == '9900') & (self.df[1] == rubrica))]

        # Adicionar uma linha em branco no final
        self.df = pd.concat([self.df, pd.DataFrame([[''] * len(self.df.columns)], columns=self.df.columns)], ignore_index=True)
         
