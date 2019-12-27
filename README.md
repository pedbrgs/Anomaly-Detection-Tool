# Anomaly Detection Tool
"[Visual Pattern Recognition](http://www.dcc.ufmg.br/Pos-graduacao/pesquisa/gruposdet.php?numaut=23)" course (DCC831) - Graduate Program in Computer Science ([PPGCC](http://ppgcc.dcc.ufmg.br/en/)/[UFMG](https://ufmg.br/international-visitors)). 

Professor: [William Robson Schwartz](http://william.dcc.ufmg.br/).

## Problem description

Implement a method that, given an input image like those shown in Figure 1, detects anomalous regions ([Instructions in Portuguese](https://github.com/pedbrgs/anomaly-detection-tool/blob/master/Instructions-PT.pdf)).
<figure>
  <p align="center">
  <img src="https://lh3.googleusercontent.com/hdlfclJcMhlk-XVyAbQVHiTIIHiCJv26taLixGv-gVu3QjWpZrjne5gZYbck612hZ8b6FcuDo_0C2aWJnQomybtnj45hMoavur5mP7V6zMNhwGsQu1wZncxfgGw5IYVdnUUfqbexmw-EU2KaOa7YhlAyBaqL_hV0dXtWMaOlXgN5k4mNtnukP4DlzV3pfLaPTLbmN64Rs7GZgGePRKlPejJb1Dco8WUomJP8AMgJlQAihep8JhhA1NbXXFZio41XN-942Eak317FoYIlpeOPc_3ycfxJNE-rtDTGi9Qv5p5_0s7Y31o4PLHfIkDw6HMhWnxpHsSfMRmy9Q1Q1Pn7d888R6aWI38jGb52PMFA1s6kuD_CmceOfpKdsucGQMB60c9UiuC19E4eIw5vrfe4DBD36JwzJC4vv1VmJniPsO7HHDnFCdSGf4AgZewSlauf8lAmtPuO6viWsZVYMFy-E_ojx8kEcOduIIKbJ7yT6vSwMCMoe3aMcCwOgnzKwkrpGofwPzOixw7sI8UxNZPOxELXmrWCd7suTtxOZFUgRuATRMGkiyCvAjduifeRupNl9K_ndxAaDxnxXJlQpni92N6-amL9BEncbPsme-XLzaSfcePGQKD3BlTJYnaTp7bTtBViV58hWyJTvp8m9RR-89jnGLLvgmyxrSdZpW3wGd0R45C1VLbk4hBU=w600-h450-no" width="425"/> <img src="https://lh3.googleusercontent.com/cGZ__XMDjEG7Hr83kUQ-oEndZxHXusOeeyHb6eNvMTd9yDBG_rpENWwcQuoefmPXs6QTJPNZ3g6xhJF-FACpM_IQBWZwQk_g-xnQty4Mk-_CcJbrE9wjNXrAwQV0hd3HDoZHqyzfXV05kot9PMNGUcYijnp6rBALXEROih8na4vp2l7fu3UrhIexncf5XgOB1cc8sgs08mGG3KRoesEwj3FyPEG9vYsnWlkzMynDT8qv8taGpS2oRb74MyhGW3ClO3T5cnW1W43f1Twqs26LV0uuRhSofywNzTnt2gitogPXuMxD2VR_hMQnB7sCm4F9ohQ6x9rUXQT_9y2eYS5yc6suCYUKb9lVVAn_WIR6JEJJUtXOZdscQvGH_JDLblOTprGfyuQb8jepdku4h-euqt-zUSYKYpJ14rej5pr6UUapfc0VGz7ZwW4GQ3SxnEAT35J3HaiNXmuxNAyicg3eTrerZAzCKXYOuL0DETM0u7FK6IBg7JGMVaZ8Utq9itayQWRYYfpeUqgyZPCtPHMiZ2h01CHbHUb9AsnoOglKa22zxzXGObVrZoTwSRn6HdgZrB20GnAB7odKTtqIgCHxT3icf47H73KixreLT1EiKlt07DrE_Z6YaBlVVzFGVnh5OfnrW7RH76HVH88ZEBBTWDWgOgSPPmJFBfyT80S0EkAc7TEGf_x7HJlX=w595-h446-no" width="425"/> 
  <figcaption><p align="center">Figure 1: Input image examples.</p></figcaption>
  </p>
</figure>

## Proposed approach

<figure>
  <p align="center">
    <img src="https://lh3.googleusercontent.com/MaqtdIHE4zBiS6h3HK-08JvfR3ZhJXrPmS-4QUms_FQ5hH12L3SDImyyWY9thcfTmPaIGlxLcQNv2oSW_jN4gZo43w354Qe10qnIM_JdwAYz5OJlCOGC631wk3NJT89LpjCRpEl1izle0Y7a4WjfDWxwdTUc8OJdidJ_S2J6Oe7dQMBfh_ZXQPHUmBQx7WRZ_NSEV35JOEqo86eOUMk7EgHqG80kGsUsXmb48-Im6gm8RydRNp9L3FjeItpLVKfgQpuS33_7TkOyZSSaKEQZsAy1b6rdzDrwU-S8CrgRmSw8K-u5wlGuwIM3ax08FTVajMXv5EmIJe4qPX8DhZl5K6EY22cZB-DXQxYR7VdzBVKj1Qr8kIvZuT9n6U4a7dmeJTmEFMe0XRQIBE8WYJDZqQu-8qUKXWTNSKuMjI-PSix0RB29ewJPW4P3EXWnFwn9MIp9sspBkMgSzJqFJ37W72T02qru8COa-u5QhTROMMszP_09oTzEHpemgV77eOFGx-Np52HrQmOOsT7tcTgHCpnvyeMFL-fOHsy-sbj3jw8Xszx_-RRNIzlXmXwWyzrMq9EhBp75gD23UgAYEqU3NLvGcgxM8TqFcsGXLgDkL46cyMpJxufMXAWtPqMmbWqMSlSxdXywIopIeOM_GiZ6lZycgJs75F-rkneHC7E2IZQDKsxVbasXjT7X=w526-h525-no" width="40%">
    <figcaption><p align="center">Figure 2: Object segmentation through morphological filtering.</p></figcaption>
  </p>
</figure>

<figure>
  <p align="center">
    <img src="https://lh3.googleusercontent.com/jGRXGXgD3bvUFdILVK7B-4hPxjJ_eJWz3fFCChyDHqxMryyqCpmJrtsYt1biojkN-m1uHZktmk2vXCifJyehKIIfydp7jPr1BTD2k9tpEe4z2wlHGfpxv_VJGYtBJUWOBUuQv9Y7dgn_hw0BNRcRkx35VbwcqfqvRngaDGqcrRmbaNN81Yy3fBn4muJe2c0Il28YzPOUsbSVW2OhhhKbZ0StbFMY7BuAo0zj2CAJcUFjEGuMn2BjaPdfCxkeoX-y59dYVzGcYtJ9Z0PksZcPvJ6cjJfXBfPYYTbp9AWqIRwziT44Q2G6uGvRcx0hDLYaBteo6uhMAcoJEPb_yXFEkEO1JIGEN0lJnIA5_p_rje62jzbM7vMNF2HXLHB3mX9IKceT1USjLgg9wZkRVqoWJjTUcBVSyyo_uxCMZY-alXWoDuvcukQMhja2p5mIZgKITpdtrUUyyHemarUILj0TxLMWZuY7CDwuPcM-EUHMoEtVnZAslRGX7AUftQcqXsiTD0z2_PnrHq6llRZCLv_D9LUPN95W5KaeXdfUzR5W2CJICDDlX_Y9u0JZjDtz4Uo51jeKqt7RmPrEcFVkSFjwbWl6FXaLigZPhcUF42qDrOACO5M5RYlum8UVVT46YJWesuJUdBZpfBrO-VEUOriwAeUZLUIFe9zFT3_TVrqCoxNA5Odn7qKjxgKb=w1182-h268-no" width="95%">
    <figcaption><p align="center">Figure 3: Feature extractor based on <a href="https://arxiv.org/pdf/1512.03385.pdf">ResNet-34</a>.</p></figcaption>
  </p>
</figure>

### Requirements
* Python 3.6.8
* OpenCV 4.1.0
* Torch 1.3.0

### Running code

`python3 detector.py --data data/<input image>`

### Results

<figure>
  <p align="center">
  <img src="https://lh3.googleusercontent.com/7EtlsGXYBieGjqVZMgzstvJD_GREUN_GjuiJUONrUvqG7n4AYUoYAtl9sAAdjTw_f1tKr02EJw02M-ji59S6QYUvWS_VDwgiE_rOwEqqvSIftelvdF3_Hk_GDIjhlF_TlndVYI6o-DNXkviU2pJABYdv0uvIu6Y3xLgxBVMVDgmPONI6bSDOMX5GM3bsSI_iYBP1UPS3jhpniA7ezZMibRnl3W1OeCNw7Vm3Q95L9_bdrpaX0JOdwCtttJH9Cs07jos0YCk08PpzyGzHxocJtfkken4XKMjMTUdLDD4_465yKzKU6ERAz11_NyNPSNKK46XRzVCYp3hxQ-jBQC62jV8rK12L7TNsbAbnbM_P2M8kAxgA-9BtM7BITypYKWaj5eP5kYmGOKh79JFp7OqN6ER8BN7jE3WtXjh1-0ZMEwbTYmW6WhH93UfN6xmGZV7cJ4G23yLR-5fz9re0riOPkHCrUYitEAAGxN8Nd1UiRlpc-u445pSigdzDe-dXjOm39oret7_OdWmu0T-bSJIkpyDiectUiKT0knmPDx5Dw_so52QhcD5ul8DcD5tHMbkmIBmbT6WTH13AjRfLrKFcrE9xxZFMrRL1r3MvEqC4B_mTok7JkNkgK37TUDYA8PdDoTY0pcEFY-6SSxIpoQe2YIFlrJLPXhKZpfDQci4iKvcg_EUc9yhihkp-=w600-h450-no" width="425"/> <img src="https://lh3.googleusercontent.com/H3Fa4M47KmxasW0Pz7H7guVbINX1lhio0pvxyQjA7MJ-hiklwee-BUyeslKyxu9Yyu3bNV0ZVV3VKoEEdxt0m8zMz1jzQ1TuRsxthhEL8u6QHFwaJN3CYG5XE_lFsUA_eu44aNGt09E_AcYkPf6qpiPubrPj-SAEk-EpxI0_t-7Bn53eqtL4qWvPxDFaTQfKm7EBWDXRvSlx0A3YMzQrK_kf3T64quM1LX6dwZv3Pkw1lmKOwHNEDHk3QyzEbOBLjIZDzVBOfaIJ5LTvHtyv2t3NqKTR1_0vgxNh9mpsKaUvaqD4Xngt9Ak-jWIbnCOZmuQRNYTSBFGdJn4GLMw6dnMamrYgIRr_CczOe00XuqHsdBKdLkVPk4ARs2DYGuQwstg2z_GnZHXw1z_ndfWysf3Xxsm3kviz4VqYaglQODO21nj00C2hj0oxdqdD7jTYW7hfB00cNtkuVYNHnnsxO_GbvQi1kX0mAYmqcKfWVPqABxnVMgOhnOsNupatf9-luggdHCZaxpXMHHca_Hc-FGMo_yHyqVf166F6kkrE5Q_Mtjz6lvRw1geKy49C1yaR9UztStxHHj84aWT4oKbkel2YIMSuPPC7JlLN0AIkKMOHUhyrVqgEwDg13WtO37CFJYTxppWJiuj43IlDUdr4fc_6ZZkOc4bUJqj-kcCX5DAqFJhbV1JaDblD=w595-h446-no" width="425"/> 
  <figcaption><p align="center">Figure 4: Output image examples.</p></figcaption>
  </p>
</figure>

For more results, go to [`results/`](https://github.com/pedbrgs/anomaly-detection-tool/tree/master/results) directory.

### Citation

```
{
  @misc{pedbrgs-adtool,
       author = {Pedro Vinicius A. B. Venancio},
       title = {Anomaly Detection Tool},
       year = {2019},
       howpublished = {\url{https://github.com/pedbrgs/anomaly-detection-tool/}}
}
```
