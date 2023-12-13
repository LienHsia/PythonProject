import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class CampusNavigationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("校园导航程序")

        # 创建图
        self.G = nx.Graph()

        # 添加边和权重
        self.add_edges()

        # 创建图形绘制区域
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=0, column=2, rowspan=4, padx=10, pady=10)

        # 创建界面元素
        self.start_label = ttk.Label(self.master, text="起点:")
        self.start_combobox = ttk.Combobox(self.master, values=list(self.G.nodes))
        self.end_label = ttk.Label(self.master, text="终点:")
        self.end_combobox = ttk.Combobox(self.master, values=list(self.G.nodes))
        self.calculate_button = ttk.Button(self.master, text="计算最短路径", command=self.calculate_shortest_path)
        self.result_label = ttk.Label(self.master, text="最短路径和权重:")

        # 设置字体为支持中文的字体
        self.set_chinese_font()

        # 布局界面
        self.start_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.start_combobox.grid(row=0, column=1, padx=5, pady=5)
        self.end_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.end_combobox.grid(row=1, column=1, padx=5, pady=5)
        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=3, column=0, columnspan=2, pady=5)

        # 一开始展示一个没有任何一条边高亮的简易图
        self.draw_campus_map([], show_weights=True)

    def set_chinese_font(self):
        # 设置字体为支持中文的字体，SimHei是中文黑体的名称
        matplotlib.rcParams['font.family'] = 'SimHei'
        matplotlib.rcParams['axes.unicode_minus'] = False

    def add_edges(self):
        edges = [
            ("North Gate", "Lan Yuan Dormitory Area", 16),
            ("North Gate", "Mei Yuan Dormitory Area", 12),
            ("Mei Yuan Dormitory Area", "Mei Yuan Restaurant", 17),
            ("Mei Yuan Dormitory Area", "He Ming Building", 29),
            ("Mei Yuan Restaurant", "He Ming Building", 15),
            ("He Ming Building", "He Rong Building", 17),
            ("North Gate", "He Ming Building", 21),
            ("He Rong Building", "Lan Yuan Dormitory Area", 23),
            ("Lan Yuan Dormitory Area", "Lan Yuan Restaurant", 16),
            ("Lan Yuan Dormitory Area", "North Playground", 32),
            ("Lan Yuan Restaurant", "North Playground", 6),
            ("Lan Yuan Restaurant", "He Jun Building", 18),
            ("He Jun Building", "He Jian Gymnasium B", 1),
            ("He Jian Gymnasium B", "Sports College", 17),
            ("Sports College", "East Gate", 12),
            ("Sports College", "School of Environmental Studies", 18),
            ("He Jian Gymnasium B", "North Playground", 40),
            ("Sports College", "North Playground", 9),
            ("He Jun Building", "School of Chemical Engineering", 8),
            ("School of Chemical Engineering", "He Yi Building", 27),
            ("Library", "He Jun Building", 15),
            ("West Gate", "Yi Fu Building", 19),
            ("Mei Yuan Restaurant", "West Gate", 31),
            ("North Gate", "He Ming Building", 24),
            ("He Ming Building", "West Gate", 21),
            ("He Ming Building", "Library", 10),
            ("He Rong Building", "Library", 20),
            ("He Rong Building", "He Jun Building", 18),
            ("He Rong Building", "Lan Yuan Restaurant", 15),
            ("Lan Yuan Restaurant", "He Jian Gymnasium B", 32),
            ("School of Environmental Studies", "East Gate", 17),
            ("School of Environmental Studies", "He Yuan", 13),
            ("He Jun Building", "School of Chemical Engineering", 8),
            ("School of Chemical Engineering", "He Jian Gymnasium A", 31),
            ("School of Chemical Engineering", "He Yuan", 32),
            ("He Yuan", "He Jian Gymnasium A", 22),
            ("He Yi Building", "Library", 20),
            ("He Yi Building", "He Zhan Building", 20),
            ("He Zhan Building", "West Gate", 11),
            ("He Zhan Building", "Library", 4),
            ("Library", "He Ming Building", 10),
            ("Library", "He Rong Building", 20),
            ("Library", "He Jun Building", 15),
            ("He Yi Building", "School of Chemical Engineering", 27),
            ("He Yi Building", "Qin Ye Building", 7),
            ("He Zhan Building", "Wen Bo Building", 5),
            ("Wen Bo Building", "Qin Ye Building", 19),
            ("Wen Bo Building", "South Playground", 12),
            ("He Zhan Building", "South Playground", 17),
            ("South Gate", "South Playground", 28),
            ("West Gate", "South Playground", 21),
            ("South Gate", "Wen Bo Building", 10),
            ("South Gate", "Qin Ye Building", 10),
            ("Qin Ye Building", "He Jian Gymnasium A", 12),
            ("South Gate", "He Jian Gymnasium A", 25),
        ]

        for edge in edges:
            self.G.add_edge(edge[0], edge[1], weight=edge[2])
            # 添加无向边
            self.G.add_edge(edge[1], edge[0], weight=edge[2])

    def calculate_shortest_path(self):
        start_point = self.start_combobox.get()
        end_point = self.end_combobox.get()

        if not start_point or not end_point:
            # 若未输入起点或终点，展示一个没有任何一条边高亮的简易图
            self.draw_campus_map([], show_weights=True)
            self.result_label.config(text="请输入起点和终点")
            return

        try:
            path = nx.shortest_path(self.G, source=start_point, target=end_point, weight='weight')
            weight = nx.shortest_path_length(self.G, source=start_point, target=end_point, weight='weight')
            result_text = f"最短路径从 {start_point} 到 {end_point}：\n路径：{path}\n权重：{weight}"

            # 绘制地图并高亮显示路径
            self.draw_campus_map(path, show_weights=False)
        except nx.NetworkXNoPath:
            result_text = f"No path found from {start_point} to {end_point}"

        self.result_label.config(text=result_text)

    def draw_campus_map(self, path, show_weights=True):
        self.ax.clear()
        pos = nx.spring_layout(self.G)
        nx.draw(self.G, pos, with_labels=True, font_weight='bold', ax=self.ax)

        # 高亮显示路径
        edges = list(zip(path, path[1:]))
        if edges:
            nx.draw_networkx_nodes(self.G, pos, nodelist=path, node_color='r', ax=self.ax)
            nx.draw_networkx_edges(self.G, pos, edgelist=edges, edge_color='r', width=2, ax=self.ax)

            # 在路径上标示权重
            if show_weights:
                labels = nx.get_edge_attributes(self.G, 'weight')
                edge_labels = {(edge[0], edge[1]): labels[edge] for edge in edges}
                nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels, font_color='blue', ax=self.ax)

        # 刷新图形
        self.canvas.draw()


if __name__ == "__main__":
    matplotlib.use("TkAgg")
    root = tk.Tk()
    app = CampusNavigationApp(root)
    root.mainloop()
