#
import my_module

print ("hello world")


x = my_module.summa(1.6, 2)

#print(x)
if __name__ == '__main__':
    print('самостоятельный запуск')
else:
    print(__name__, 'был импортирован')