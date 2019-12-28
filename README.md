# Anomaly Detection Tool
"[Visual Pattern Recognition](http://www.dcc.ufmg.br/Pos-graduacao/pesquisa/gruposdet.php?numaut=23)" course (DCC831) - Graduate Program in Computer Science ([PPGCC](http://ppgcc.dcc.ufmg.br/en/)/[UFMG](https://ufmg.br/international-visitors)). 

Professor: [William Robson Schwartz](http://william.dcc.ufmg.br/).

## Problem description

Implement a method that, given an input image like those shown in Figure 1, detects anomalous regions ([Instructions in Portuguese](https://github.com/pedbrgs/anomaly-detection-tool/blob/master/Instructions-PT.pdf)).
<figure>
  <p align="center">
  <img src="https://i.ibb.co/wKCFnRq/img1-1.jpg" width="425"/> <img src="https://i.ibb.co/HgHhpCv/img5-1.jpg" width="425"/> 
  <figcaption><p align="center">Figure 1: Input image examples.</p></figcaption>
  </p>
</figure>

## Proposed approach

<figure>
  <p align="center">
    <img src="https://i.ibb.co/L5BjPkK/process.png" width="40%">
    <figcaption><p align="center">Figure 2: Object segmentation through morphological filtering.</p></figcaption>
  </p>
</figure>

<figure>
  <p align="center">
    <img src="https://i.ibb.co/pPhLj0h/Resnet34-Modified.png" width="95%">
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
  <img src="https://i.ibb.co/9qQMMhb/img1.jpg" width="425"/> <img src="https://i.ibb.co/F86jcy7/img5.jpg" width="425"/> 
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
