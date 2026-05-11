import np
import pd
import plt

df = pd.read_csv("")
df.head(10)
df.tail(10)

no_fv = data['F v(D admin)'].sum()
f_tp = no_fv
no_fv = '{:,0f}'.format(no_fv)
plt.pie([mtp,ftp],labels=[male,female],colors=[#,#],autopct='%0.0f%%',startangle=90,radius=2)
plt.legend(loc='best,figsize=12)
plt.show()

stv_v['tot'] = stv_v['tot'].str.replace(',','')
stv_v.plot(kind='bar',figsize=(12,10))
plt.show()