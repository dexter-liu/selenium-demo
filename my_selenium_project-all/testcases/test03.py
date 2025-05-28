# python3.6.5
# 需要引入requests包 ：运行终端->进入python/Scripts ->输入：pip install requests
# from lib.ShowapiRequest import ShowapiRequest
#
# r = ShowapiRequest("http://route.showapi.com/184-4","272526","a924d4e982ae404b8a068b4d1c7784f2" )
# r.addFilePara("image", "test.png")
# r.addBodyPara("typeId", "34")
# r.addBodyPara("convert_to_jpg", "0")
# r.addBodyPara("needMorePrecise", "0")
# res = r.post()
# result = res.text
# print(result)
# body = res.json()['showapi_res_body']
# print(body['Result'])
# print(res.text) # 返回信息
# 478Ed090Be1f45E78E6CeB1e1a297987

# 以上代码已经不适用了，新的个人实现，请查看下方代码

from lib.chaojiying import Chaojiying_Client

chaojiying = Chaojiying_Client('dexterliu', '2019Sep!', '969807')
im = open('/Users/dexter/geektime/Selenium/Demo/my_selenium_project-all/test.png',
          'rb').read()
print(chaojiying.PostPic(im, 8001))
verify_code = chaojiying.PostPic(im, 8001)['pic_str']
print(verify_code)
