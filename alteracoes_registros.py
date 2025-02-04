import pandas as pd
import numpy as np

class AlteracoesRegistros():
    
    def __init__(self, df):
        self.df = df
        
    def alterar_F500(self):
        self.df.loc[self.df[0] == 'F500', 2] = '06'
        self.df.loc[self.df[0] == 'F500', 7] = '06'
    
    def alterar_F525(self):
        self.df.loc[self.df[0] == 'F525', 7] = '06'
        self.df.loc[self.df[0] == 'F525', 8] = '06'
    
    def zerar_M200(self):
        self.df.loc[self.df[0] == 'M200', 1:12] = '0'

    def zerar_M600(self):
        self.df.loc[self.df[0] == 'M600', 1:12] = '0'

    def alterar_M400(self):
        self.df.loc[self.df[0] == 'M400', 1] = '06'
    
    def alterar_M800(self):
        self.df.loc[self.df[0] == 'M800', 1] = '06'
    
    def alterar_M410(self):
        self.df.loc[self.df[0] == 'M410', 1] = '920'
    
    def alterar_M810(self):
        self.df.loc[self.df[0] == 'M810', 1] = '920'
    
    def excluir_M210(self):
        self.df = self.df[self.df[0] != 'M210']
    
    def excluir_M610(self):
        self.df = self.df[self.df[0] != 'M610']

    # Arquivo não consolidados

    def alterar_A170(self):
        colunas = [10, 11, 14, 15]
        self.df.loc[self.df[0] == 'A170', colunas] = '00'
        self.df.loc[self.df[0] == 'A170', [8, 12]] = '06'
    
    def alterar_C170(self):
        colunas = [10, 11, 14, 15]
        self.df.loc[self.df[0] == 'C170', colunas] = '00'
        self.df.loc[self.df[0] == 'C170', [8, 12]] = '06'
        
    def alterar_A100(self):
        colunas = [15, 17, 18, 19]
        self.df.loc[self.df[0] == 'A100', colunas] = '00'

    def alterar_C100(self):
        colunas = [15, 17, 18, 19]
        self.df.loc[self.df[0] == 'C100', colunas] = '00'
    
    def adicionar_registros_M(self):
        """
        Adiciona os registros M400, M410, M800 e M810 dentro do bloco de registros M
        respeitando a ordem numérica correta.
        """

        # Captura o valor do campo 1 do registro 'F550' (não deve ser uma série)
        valor_registrosM = self.df.loc[self.df[0] == 'F550', 1]
        valor_registrosM = valor_registrosM.iloc[0] if not valor_registrosM.empty else '0'

        # Estrutura padrão dos registros M
        registros = [
            ["M400", "06", valor_registrosM, "411", "RECEITA DO PERSE"],
            ["M410", "920", valor_registrosM, "411", "RECEITA DO PERSE"],
            ["M800", "06", valor_registrosM, "411", "RECEITA DO PERSE"],
            ["M810", "920", valor_registrosM, "411", "RECEITA DO PERSE"]
        ]

        # Verificar o número total de colunas do DataFrame
        num_colunas = self.df.shape[1]

        # Encontrar a posição correta para inserir os registros dentro do bloco M
        indices_m = self.df.index[self.df[0].str.startswith('M')]
        
        if not indices_m.empty:
            idx_m_fim = indices_m.max()  # Última posição do bloco M
        else:
            idx_m_fim = 0  # Se não houver registros M, adicionar no começo

        for registro in registros:
            if not (self.df[0] == registro[0]).any():
                # Criar uma nova linha preenchendo as colunas restantes com ''
                nova_linha = registro + [''] * (num_colunas - len(registro))
                
                # Adicionar a nova linha dentro do bloco M, respeitando a sequência
                self.df = pd.concat([
                    self.df.iloc[:idx_m_fim + 1],  # Parte antes da posição correta
                    pd.DataFrame([nova_linha], columns=self.df.columns),  # Nova linha
                    self.df.iloc[idx_m_fim + 1:]  # Parte após a inserção
                ], ignore_index=True)

                # Atualizar o índice para garantir a ordem correta na próxima inserção
                idx_m_fim += 1

        # Agora adicionamos a contagem correta em 9900
        #self.atualizar_contador_9900()

    # def atualizar_contador_9900(self):
    #     """ Atualiza o contador de registros 9900 """

    #     # Contar quantas vezes cada tipo de registro aparece
    #     contagem_registros = self.df[0].value_counts().reset_index()
    #     contagem_registros.columns = ["Registro", "Quantidade"]

    #     # Remover registros existentes do tipo 9900
    #     self.df = self.df[self.df[0] != "9900"]

    #     # Criar novas linhas do tipo 9900 com os valores corretos
    #     novos_registros_9900 = [
    #         ["9900", registro, str(quantidade)] for registro, quantidade in contagem_registros.values
    #     ]

    #     # Adicionar os novos registros 9900 no local correto (antes de 9999)
    #     idx_9999 = self.df.index[self.df[0] == "9999"].min()

    #     self.df = pd.concat([
    #         self.df.iloc[:idx_9999],  # Parte antes de 9999
    #         pd.DataFrame(novos_registros_9900, columns=self.df.columns),  # Novos registros 9900
    #         self.df.iloc[idx_9999:]  # Parte depois de 9999
    #     ], ignore_index=True)

    #     print("✅ Contadores 9900 atualizados corretamente!")

