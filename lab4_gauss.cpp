#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
const int n = 6;
void showSLAY(double a[n][n], double a1[n][n], double b[n], double b1[n]) { // функция, которая выводит исходную СЛАУ на экран
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (a[i][j] >= 0) cout << " ";
            cout << a[i][j] << "\t";
        }

        cout << "=\t";
        if (b[i] >= 0) cout << " ";
        cout << b[i];
        cout << "\n";
    }
    cout << "\n\n";
}
int main()
{
    int i, j, im, k; // вспомогательные переменные
    system("chcp 1251"); // русская кодировка
    system("cls"); // очистка консоли

    /*
    а1 - приводящаяся к треугольному виду
    b1 - вектор правой части уравнения
    x  - вектор решений
    */
    double a1[n][n], b1[n], x[n];

    //Левая часть уравнений 
    double a[n][n] =
    { //var 1
    {-8, 8, 7, -7, 1, -3},
    {8, 3, 6, 2, -5, 3},
    {-8, -9, -7, 5, 7, 7},
    {6, -2, -9, -5, -1, 7},
    {7, -3, -7, -6, 2, -7},
    { 5, -4, 8, -7, -5, 3}
    };

    double aa[n][n] =
    { //var 1
    {-8, 8, 7, -7, 1, -3},
    {8, 3, 6, 2, -5, 3},
    {-8, -9, -7, 5, 7, 7},
    {6, -2, -9, -5, -1, 7},
    {7, -3, -7, -6, 2, -7},
    { 5, -4, 8, -7, -5, 3}
    };
    //Правая часть уравнений
    double  b[n] =
    { -33,149,-116, 89,-14,186 };
    double  bb[n] =
    { -33,149,-116, 89,-14,186 };
    for (i = 0; i < n; i++) // Создание дубликатов матриц ВСЕ! и так все работает
    {
        for (j = 0; j < n; j++) {
            a1[i][j] = a[i][j];
        }
        b1[i] = b[i];
    }
    //Вывод СЛАУ на экран
    cout << "Система линейных алгебраических уравнений\n\n";
    showSLAY(a, a1, b, b1);

    double tmp;
    for (k = 0; k < n - 1; k++) // прямой ход
    {
        im = k;
        for (i = k + 1; i < n; i++) //нахождение наибольшего коэффициента
        {
            if (fabs(a[im][k]) < fabs(a[i][k]))
            {
                im = i;
            }
        }

        if (im != k) // перестановка строк местами, если элемент равен нулю
        {
            for (j = 0; j < n; j++)
            {
                tmp = a[im][j];
                a[im][j] = a[k][j];
                a[k][j] = tmp;
            }
            tmp = b[im];
            b[im] = b[k];
            b[k] = tmp;
        }
        showSLAY(a, a1, b, b1); 
        
        for (i = k + 1; i < n; i++)
        {
            tmp = a[i][k] / a[k][k]; //деление верхней строки на нижнюю
            a[i][k] = 0;
            b[i] = b[i] - tmp * b[k];
            if (tmp != 0)
                for (j = k + 1; j < n; j++)
                {
                    a[i][j] = a[i][j] - tmp * a[k][j]; //вычитание из нижней строки верхней
                }
            showSLAY(a, a1, b, b1);
        }
        showSLAY(a, a1, b, b1);
    }
    cout << "Треугольный вид\n\n";
    for (i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (a[i][j] >= 0) cout << " ";
            cout << setprecision(5) << a[i][j] << "\t";
            a1[i][j] = a[i][j];
        }
        cout << "\n";
    }
    cout << "\n";
    double s = 0;
    // обратный ход
    x[n - 1] = b[n - 1] / a[n - 1][n - 1]; // первый шаг
    for (i = n - 2, j; 0 <= i; i--)
    {
        s = 0;
        for (j = i + 1; j < n; j++)
        {
            s = s + a[i][j] * x[j]; // подстановка найденных x
        }
        x[i] = (b[i] - s) / a[i][i];
    }


    cout << "Корни уравнения:\n";
    for (i = 0; i < n; i++)
        cout << "x[" << i << "]=" << x[i] << endl;

    // Подстановка в левую часть уравнения найденных x
    double h[n];
    for (i = 0; i < n; i++) {
        h[i] = 0;
        for (j = 0; j < n; j++)
            h[i] += x[j] * a1[i][j];
    }

    double row_res = 0;
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            row_res += (aa[i][j] * x[j]);
            // if (j != n-1) {
            //     cout << aa[i][j] << "*" << x[j] << " + ";
            // } else {
            //     cout << aa[i][j] << "*" << x[j] << " = " << bb[i] << endl;
            // }
        }
        cout << row_res << " = " << bb[i] << endl;
        row_res = 0;
    }

    
    return 0;
}

