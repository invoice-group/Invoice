## Invoice-发票报销工具

### 项目介绍
> 当前市场上正规发票的种类有限，但在整理发票时需要花费较多时间，当前可以结合深度学习，图像识别技术，对每种发票进行拍照实现关键信息的提取，自动进行发票整理，并对发票进行归档，方便进行财务报销和管理,有的发票上附带有二维码识别，则可以够通过二维码读取信息，直接读取信息输入到管理系统中。如果发票上二维码没有对应信息，则通过图像识别发票上的金额等具体信息输入到管理系统。 

### 项目成果展示
* 移动端

![image](https://github.com/invoice-group/Invoice/blob/master/pics/%E5%9B%BE%E7%89%872.png)
![image](https://github.com/invoice-group/Invoice/blob/master/pics/%E5%9B%BE%E7%89%873.png)

* 后台

![image](https://github.com/invoice-group/Invoice/blob/master/pics/%E5%9B%BE%E7%89%874.png)

### 应用技术说明
*  二维码识别：qrcode
*  图像分块及识别：keras
*  深度学习图片文字定位：ctpn
*  深度学习图片文字识别： crnn 
*  前端：webapp(html5+js)、hbuilder
*  后台管理系统：django





