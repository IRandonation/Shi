#include<iostream>
#include<fstream>
#include<cstdlib>
using namespace std;
//get_from_file函数从磁盘读入字符，将其中的小写字母改为大写字母，然后存回
void get_from_file()
{
	char ch;
	ifstream infile("bat.stl",ios::in);
	//定义输入文件流outfile，以输入方式打开磁盘文件f2.dat 
	if(!infile)
	{
		cerr<<"open bat.stl error!"<<endl;
		exit(1); 
	}
	ofstream outfile("f3.dat");
	//定义输出文件流outfile，以输出方式打开磁盘文件f3.dat 
	if(!outfile)
	{
		cerr<<"open f3.dat error!"<<endl;
		exit(1); 
	}
	while(infile.get(ch))	//当读取成功时，执行下面的符合语句 
	{
		
		cout<<ch;			//同时在显示器输出 
	}
	cout<<endl;
	infile.close();
	outfile.close(); 
} 
int main()
{
	get_from_file();
	//调用get_from_file(),从磁盘打开文件，并操作，然后写回磁盘
	return 0; 
}