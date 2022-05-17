from requests import get
import json
import os


class CFG:
    pdf = ['Custom_PDF'] # CustomPDF 키
    deck = ['Deck', 'CardCustom', 'Card', 'DeckCustom', 'back'] # CustomDeck 키
    image = ['Custom_Board', 'Custom_Tile', 'Custom_Token', 'Figurine_Custom'] # CusomImage 키
    bag = ['Bag'] # ContainedObjects를 사용함


def download(url, file_name):
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)


def json_read(name):
    with open(name, 'r', encoding = 'UTF8') as f:
        json_data = json.load(f)
    return json_data


def make_link(json_data, mode = True):
    tmp = []
    pdf = []
    json1 = json_data['ObjectStates'] if mode else json_data
    for j in json1:
        if j['Name'] in CFG.pdf:
            pdf.append(j['CustomPDF']['PDFUrl'])
        elif j['Name'] in CFG.deck:
            tmp_key = list(j['CustomDeck'].keys())
            tmp_link = []
            for key in tmp_key:
                tmp_link.append(j['CustomDeck'][key]['FaceURL'])
                tmp_link.append(j['CustomDeck'][key]['BackURL'])
            tmp.extend(tmp_link)
        elif j['Name'] in CFG.image:
            tmp.append(j['CustomImage']['ImageURL'])
        elif j['Name'] in CFG.bag:
            json2 = j['ContainedObjects']
            tmp_links, _ = make_link(json2, False)
            tmp.extend(tmp_links)
    return list(set(tmp)), list(set(pdf))


def download_image(file_name, save_path):
    os.chdir(save_path)
    json_data = json_read(file_name)
    links, pdf_links = make_link(json_data)
    
    for l, i in zip(links, range(len(links))):
        download(l, str(i).rjust(4, "0") + ".png")
        
    for l, i in zip(pdf_links, range(len(pdf_links))):
        download(l, "_" + str(i).rjust(2, "0") + ".pdf")

    return True

