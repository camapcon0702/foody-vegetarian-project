import requests
import json
import time
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

def crawling_all_restaurants():
    all_items = []
    page = 1

    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "vi,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
        "priority": "u=1, i",
        "referer": "https://www.foody.vn/da-nang/an-chay?CategoryGroup=food&c=an-chay",
        "sec-ch-ua": '"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
        "x-foody-user-token": "oPjr3RPDZWIKfM8TuUDUazyWmeQpmPyK1wuUBgHjqbcAuSov7XXbox2bsDkc",
        "x-requested-with": "XMLHttpRequest"
    }

    cookies = {
        "bc-jcb": "1",
        "flg": "vn",
        "__ondemand_sessionid": "4lakivemzth2y1koifraih1j",
        "gcat": "food",
        "_fbp": "fb.1.1747654853851.643706100642786130",
        "_ga": "GA1.2.999930879.1747654854",
        "_gid": "GA1.2.1453021672.1747654854",
        "__utmc": "257500956",
        "__utmz": "257500956.1747654855.1.1.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not provided)",
        "floc": "219",
        "fd.keys": "",
        "ID_FOODY.AUTH": "7F1719DA0223671169970A3F173C706692E315E2214B2E692E6CCB3A730A4508CA88DC02160208936F1555DB44B7979408B60EF6165AFDE6D512F5ACAB71B0A16116DDD9936A59A63C68790CC2470EE23ABD387666A6C3ED9F7A16AB6ECA8741B6CAB4E58DA727ECD5BB128712EB480ADA55666BF87C423CCD8EFEACADA634F45D42AB2E7F9730F64601F3C150624F7C4F40357BDEA04DDF30EBA9BA34B5DF98973287CDC27933E79A6CC373AA639B98EC01116A483954A94CCEAE5EAD6960FCDF1719AD329174BD87065235801CB8463E7FBE64A1D065C0D851F612AEF9A77E1ADAB616FB16FD6091A0DD923E4B075F2F92752417AD46C75E96F3A327E9D6F3",
        "FOODY.AUTH.UDID": "00406659-d530-443f-bf72-1ac93852f0c3",
        "FOODY.AUTH": "ADC505BFD0E8DDCA32AAE2B3FDF053F3986EB06EACD3C4E7BB5BBC41D75B67620402961215202E70AC89B2CCE21A6DB7E62497CCEA09AA161F690B3740E9B8B886AD07AB59DC6B8CF13FD4D16E569F22ADC0B759970D21037BC3FE8DB99551D6D433F4DE03B11CF0FBFE7FBAA86E4DDDE75DDA84E47FD6D0F572375CAA67A5605F10E508782955CAD4415DE67DEBBC47CFB8C33891DF0A51BE1279176264D292E46AC785D7CE61848ADEC9B23343C8F6D50713818F53EF39D61D7B7E4688D0ADFC92DC165CF5C5F1D5A0292493F125D1F7F9850C6F8D3CCA376B28188725F778FACBC5345578CB1AE8B49253F0C4F1F0789334FAC015406C2A562125C41E4E6E",
        "fd.verify.password.47220698": "19/05/2025",
        "fd.res.view.219": "12488,642488",
        "__utma": "257500956.999930879.1747654854.1747660405.1747663733.3",
        "__utmt_UA-33292184-1": "1",
        "_gat": "1",
        "__utmb": "257500956.6.10.1747663733",
        "_ga_6M8E625L9H": "GS2.2.s1747663730$o3$g1$t1747665132$j60$l0$h0$d8GJz6BKrrYjeIJqDtp6m6iE9KadoalKBCA"
    }

    while True:
        url = f"https://www.foody.vn/da-nang/an-chay?ds=Restaurant&vt=row&st=1&c=56&page={page}&provinceId=219&categoryId=56&append=false"
        print(f"Đang lấy trang {page}...")

        response = requests.get(url, headers=headers, cookies=cookies)

        if response.status_code == 200:
            try:
                data = response.json()
                items = data.get("searchItems", [])
                if not items:
                    print("Không còn dữ liệu, dừng lại.")
                    break

                for item in items:
                    filtered = {
                        "Id": item.get("Id"),
                        "Name": item.get("Name"),
                        "Address": item.get("Address"),
                        "District": item.get("District"),
                        "AvgRating": item.get("AvgRating"),
                        "DeliveryUrl": item.get("DeliveryUrl")
                    }
                    all_items.append(filtered)

            except Exception as e:
                print(f"Lỗi đọc JSON: {e}")
                break
        else:
            print(f"Lỗi HTTP: {response.status_code}")
            break

        page += 1
        time.sleep(3)

    output_path = os.path.join(BASE_DIR, 'data', 'restaurants.json')

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_items, f, ensure_ascii=False, indent=4)

    print(f"Đã lưu {len(all_items)} nhà hàng vào 'restaurants_data.json'.")
    

def crawling_all_dishes():
    input_path = os.path.join(BASE_DIR, 'data', 'restaurants.json')
    with open(input_path, 'r', encoding='utf-8') as f:
        restaurants = json.load(f)

    all_restaurant_menus = []
    all_ids_seen = set() 

    for i, restaurant in enumerate(restaurants):
        restaurant_id = restaurant.get('Id') 
        if not restaurant_id:
            continue

        url = f"https://gappapi.deliverynow.vn/api/dish/get_delivery_dishes?request_id={restaurant_id}&id_type=1"

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "vi,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
            "origin": "https://www.foody.vn",
            "priority": "u=1, i",
            "referer": "https://www.foody.vn/",
            "sec-ch-ua": '"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
            "x-foody-api-version": "1",
            "x-foody-app-type": "1004",
            "x-foody-client-id": "",
            "x-foody-client-language": "vi",
            "x-foody-client-type": "1",
            "x-foody-client-version": "1"
        }

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                menu = []
                json_data = response.json()
                menus = json_data.get("reply", {}).get("menu_infos", [])
                for info in menus:
                    dishes = info.get("dishes", [])
                    for dish in dishes:
                        dish_id = dish.get("id")
                        if dish_id not in all_ids_seen:
                            photos = dish.get("photos", [])
                            image_url = photos[0].get("value") if photos else None
                            menu.append({
                                "IdDish": dish_id,
                                "name": dish.get("name"),
                                "price": dish.get("price", {}).get("value"),
                                "image": image_url,
                                "description": dish.get("description")
                            })
                            all_ids_seen.add(dish_id) 
                print(f"[{i + 1}/{len(restaurants)}] Got {len(menu)} unique dishes from restaurant ID {restaurant_id}")
                all_restaurant_menus.append({
                    "restaurant_id": restaurant_id,
                    "menu": menu
                })
            else:
                print(f"[{i + 1}/{len(restaurants)}] Failed to fetch for restaurant ID {restaurant_id}: {response.status_code}")
        except Exception as e:
            print(f"[{i + 1}/{len(restaurants)}] Error: {e}")

        time.sleep(0.5)
    
    output_path = os.path.join(BASE_DIR, 'data', 'menus.json')

    with open(output_path, 'w', encoding='utf-8') as f_out:
        json.dump(all_restaurant_menus, f_out, ensure_ascii=False, indent=2)

    print(f"Đã lưu menu của {len(all_restaurant_menus)} nhà hàng vào 'data/menus.json'")

