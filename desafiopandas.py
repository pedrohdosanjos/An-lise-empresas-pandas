import pandas as pd
import matplotlib.pyplot as plt

# leitura dos arquivos.
enderecos = pd.read_csv("DadosEndereco.csv")
empresas = pd.read_csv("DadosEmpresa.csv")

# filtrando empresas com a opcao_pelo_simples = SIM.
aff_option = empresas.loc[empresas["opcao_pelo_simples"] == "SIM"]
aff_option.reset_index(inplace=True, drop=False)
aff_option.to_csv("Empresas_opcao_simples.csv")

# guardando os cnpj's das empresas localizadas em Curitiba ou Londrina.
cwb_lon = enderecos.loc[(enderecos["municipio"] == "CURITIBA") | (enderecos["municipio"] == "LONDRINA")]

# filtrando empresas em Curitiba ou Londrina com o capital social maior que 5000.
cwb_lon_big = empresas.loc[(empresas["capital_social"] > 5000) & (empresas["cnpj"].isin(cwb_lon["cnpj"]))]
cwb_lon_big.reset_index(inplace=True, drop=False)
cwb_lon_big.to_csv("Capital_5000+.csv")

# gráfico de empresas x bairro de Curitiba
cwb = enderecos.loc[enderecos["municipio"] == "CURITIBA"]
bairros = list(cwb["bairro"])
cwb['bairro'].value_counts().plot.bar()
plt.ylabel('n° de empresas')
plt.savefig('empresasXbairros.png')
plt.show()

# Visto que ambas análises selecionam um grupo de empresas com características específicas,
# seria interessante após separá-las por cada fator, unir os fatores de localização, capital
# e opção pelo simples e registrar tais empresas.
selecionadas = cwb_lon_big.loc[cwb_lon_big["opcao_pelo_simples"] == "SIM"]
selecionadas.reset_index(inplace=True, drop=False)
selecionadas.to_csv("Selecionadas.csv")
