import numpy as np
import matplotlib.pyplot as plt

# Создаём фигуру и оси
fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)

# Рисуем единичную окружность
theta = np.linspace(0, 2*np.pi, 300)
x = np.cos(theta)
y = np.sin(theta)
ax.plot(x, y, label="Тригонометрическая окружность")

# Оси
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# Основные точки
points = [(1, 0, "0°"), (0, 1, "90°"), (-1, 0, "180°"), (0, -1, "270°")]
for px, py, label in points:
    ax.plot(px, py, 'ro')  
    ax.text(px, py, label, fontsize=12, ha='center', va='bottom')

# Угол 30° (пример)
angle = np.pi / 6
ax.plot([0, np.cos(angle)], [0, np.sin(angle)], 'g-', linewidth=2)  # Радиус
ax.plot(np.cos(angle), np.sin(angle), 'go')  # Точка на окружности
ax.text(np.cos(angle), np.sin(angle), "30°", fontsize=12, ha='right')

# Сетка и стиль
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend()
plt.show()
