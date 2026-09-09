% 1. تعريف البيانات
x = [1, 2, 3, 4];
y = [2, 2.8, 3.6, 4.5];
n = length(x);

% 2. الشروط الأولية
w = 0;
b = 0;
alpha = 0.01;
epochs = 2000;

% تحديد التكرارات المراد رسمها: تركيز على البداية + خطوات متباعدة لاحقاً
plot_iters = unique([0, 1, 2, 3, 5, 10, 15, 25, 40, 60, 100:100:epochs]);
total_plotted = length(plot_iters);

% مصفوفات لحفظ المسار
loss_history = zeros(epochs, 1);
x_plot = linspace(0.5, 4.5, 100);

% 3. الحل المثالي (polyfit)
p_opt = polyfit(x, y, 1);
y_opt = polyval(p_opt, x_plot);
optimal_loss = mean((polyval(p_opt, x) - y).^2);

% تجهيز مساحة الرسم
figure('Color', 'w', 'Position', [100, 100, 1150, 500]);
colors = cool(total_plotted); 
color_idx = 1;

% --- الرسم الأول: تطور الخط من الصفر ---
subplot(1, 2, 1);
hold on;

% رسم خط البداية تماماً (Iteration 0: w=0, b=0)
if ismember(0, plot_iters)
    plot(x_plot, w * x_plot + b, 'Color', colors(color_idx, :), 'LineWidth', 1.2);
    color_idx = color_idx + 1;
end

for iter = 1:epochs
    % حساب التنبؤ والخطأ
    y_hat = w * x + b;
    error = y_hat - y;
    loss_history(iter) = mean(error.^2);
    
    % تحديث المعاملات
    dw = (2/n) * sum(error .* x);
    db = (2/n) * sum(error);
    w = w - alpha * dw;
    b = b - alpha * db;
    
    % رسم الخط إذا كان التكرار ضمن القائمة المحددة
    if ismember(iter, plot_iters)
        plot(x_plot, w * x_plot + b, 'Color', colors(color_idx, :), 'LineWidth', 1.1);
        color_idx = color_idx + 1;
    end
end

% رسم الخط النهائي والمثالي والنقاط
h_opt  = plot(x_plot, y_opt, 'k--', 'LineWidth', 2.2, 'DisplayName', 'Optimal Fit');
h_last = plot(x_plot, w * x_plot + b, 'b-', 'LineWidth', 2.0, 'DisplayName', 'Iter 2000');
h_data = plot(x, y, 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'r', 'DisplayName', 'Data Points');

title('تطور خط الانحدار من البداية (Iter 0) حتى 2000');
xlabel('X'); ylabel('Y');
legend([h_data, h_opt, h_last], 'Location', 'northwest');
colormap('cool');
c = colorbar;
c.Label.String = 'Progression (Initial -> Converged)';
grid on; 
axis([0.5 4.5 -0.5 5]); % توسيع المحور لترى خط الصفر بوضوح

% --- الرسم الثاني: دالة الخطأ مع تدريج Logarithmic لرؤية التفاصيل ---
subplot(1, 2, 2);
semilogy(1:epochs, loss_history, 'r-', 'LineWidth', 2, 'DisplayName', 'MSE Loss'); hold on;
yline(optimal_loss, 'k--', 'LineWidth', 1.5, 'DisplayName', 'Min Loss');
title('منحنى الـ Loss بمقياس لوغاريتمي (Log Scale)');
xlabel('Iteration'); ylabel('MSE Loss (Log Scale)');
legend('Location', 'northeast');
grid on;