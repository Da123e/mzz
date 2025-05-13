from tkinter import *
from tkinter import messagebox

class Employee:
    def __init__(self, base_salary, total_employees, years_of_service):
        self.years_of_service = years_of_service
        self.total_employees = total_employees
        self.base_salary = base_salary

    def calculate_salary(self):
        calculate = 500 * self.years_of_service + self.base_salary
        return calculate

    @staticmethod
    def is_high_salary(sd):
        return sd.calculate_salary() > 10000



class on_click:
    def __init__(self, rot):
        self.root = rot
        self.total_employees = 0
        self.current_employee = 1
        self.total_salary = 0

        self.label_employees =Label(root, text="请输入员工人数：",bitmap="hourglass",bg="orange",compound="left")
        self.label_employees.grid(row=600, column=2, pady=0)
        self.entry_employees = Entry(root)# 输入员工人数
        self.entry_employees.grid(row=600, column=3, pady=0)
        self.button_submit_employees = Button(root, text="确定",bg="white",relief="flat", command=self.get_total_employees)
        self.button_submit_employees.grid(row=601, column=3, pady=0)

        self.label_base_salary = Label(root, text="")
        self.entry_base_salary = Entry(root,show="亿")# 输入基本工资
        self.label_years_service = Label(root, text="")
        self.entry_years_service = Entry(root,show="年")# 输入工作年限
        self.button_submit_info = Button(root, text="确定", relief="raised",command=self.calculate_salary,bg="lightblue")

    def get_total_employees(self):
        try:
            self.total_employees = int(self.entry_employees.get())
            if self.total_employees <= 0:
                messagebox.showerror("错误", "员工人数必须大于 0")
                self.entry_employees.delete(0, END)
                return

            self.label_employees.grid_forget()# 修改此处
            self.entry_employees.grid_forget()# 修改此处
            self.button_submit_employees.grid_forget()# 修改此处

            self.label_base_salary.config(text=f"请输入第 {self.current_employee} 位员工基本工资:",bg="lightgreen")
            self.label_base_salary.grid(row=601, column=3, pady=0)
            self.entry_base_salary.grid(row=601, column=4, pady=0)

            self.label_years_service.config(text=f"请输入第 {self.current_employee} 位员工工作年限:",bg="salmon")
            self.label_years_service.grid(row=602, column=3, pady=0)
            self.entry_years_service.grid(row=602, column=4, pady=0)
            self.button_submit_info.grid(row=603, column=4, pady=0)
        except ValueError:
            messagebox.showerror("错误", "请输入有效的整数")

    def calculate_salary(self):
        try:
            base_salary = float(self.entry_base_salary.get())
            years_of_service = float(self.entry_years_service.get())

            employee = Employee(base_salary, self.total_employees, years_of_service)
            salary = employee.calculate_salary()
            self.total_salary += salary

            salary_info = f"工资: {salary}"
            if employee.is_high_salary(employee):
                salary_info += "\n高薪"
            else:
                salary_info += "\n低薪"

            if self.current_employee == self.total_employees:
                average_salary = self.total_salary / self.total_employees
                salary_info += "\n平均工资为: {:.3f}".format(average_salary)
                messagebox.showinfo("信息", salary_info)
                self.root.destroy()# 关闭窗口
            else:
                messagebox.showinfo("信息", salary_info)
                self.current_employee += 1
                self.label_base_salary.config(text=f"请输入第 {self.current_employee} 位员工基本工资:")
                self.label_years_service.config(text=f"请输入第 {self.current_employee} 位员工工作年限:")
                self.entry_base_salary.delete(0, END)# 清空输入框
                self.entry_years_service.delete(0, END)# 清空输入框

        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字")

if __name__ == "__main__":
    root = Tk()
    root.resizable(True, True)  # 设置窗口可调大小
    root.geometry("500x350+500+200")  # 设置窗口大小和位置
    root.title("工资")
    root.configure(bg="white")  # 设置背景颜色


    on_click(root)
    root.mainloop()