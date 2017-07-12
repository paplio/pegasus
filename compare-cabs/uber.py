from uberpy import Uber
uber = Uber('XFNTHMY-KyKVI0mmJFh-ps6c4-PgX0Hj', 'ZzQ0mbOaAK2Vxv_5iEzH2nfK67Zwdb400hwuCeBU','RLxmD2O-oLUbPxfn1puVI9idx7nWD5Br0lMYUr1V')

start_latitude = 12.927963
start_longitude = 77.629086

end_latitude = 12.927960
end_longitude = 77.629082

fare = uber.get_price_estimate(start_latitude, start_longitude, end_latitude, end_longitude)
print fare.items()


