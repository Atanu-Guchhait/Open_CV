import cv2


def load():
    file_path = input("Enter file path of the image: ")
    image = cv2.imread(file_path)
    return image

def convetGrayScale(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

def show(gray):
    cv2.imshow("Showing Gray scale image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def save(gray):
    file_name = input("Enter file name to be saved")
    cv2.imwrite(f"Images\{file_name}.png")
    print(f"{file_name} saved successfully")


def main():
    image = load()
    gray_image = convetGrayScale(image)

    temp = input("For save Press 0, show Press 1 ")
    if temp==0:
        save(gray_image)
    else:
        show(gray_image)

main()
