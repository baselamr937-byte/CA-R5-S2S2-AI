% 1. تعريف البيانات
x = [1, 2, 3, 4];
y = [2, 2.8, 3.6, 4.5];
n = length(x);

% 2. الشروط الأولية
w = 0;
b = 0;
alpha = 0.01;
epochs = 100;

% مصفوفات لحفظ المسار ودالة الخطأ
loss_history = zeros(epochs, 1);
x_plot = linspace(0.5, 4.5, 100);

% 3. حساب الخط المثالي باستخدام polyfit
p_opt = polyfit(x, y, 1);
y_opt = polyval(p_opt, x_plot);

% تجهيز مساحة الرسم
figure('Color', 'w', 'Position', [100, 100, 1150, 500]);

% --- الرسم الأول: كل الـ 100 تكرار + الخط المثالي ---
subplot(1, 2, 1);
colors = cool(epochs); % تدرج لوني للتكرارات
hold on;

% رسم كل تكرار
for iter = 1:epochs
    % حساب التنبؤ والخطأ
    y_hat = w * x + b;
    error = y_hat - y;
    
    % تسجيل الـ Loss
    loss_history(iter) = mean(error.^2);
    
    % رسم خط التكرار الحالي
    plot(x_plot, w * x_plot + b, 'Color', colors(iter, :), 'LineWidth', 0.9);
    
    % المشتقات الجزئية
    dw = (2/n) * sum(error .* x);
    db = (2/n) * sum(error);
    
    % تحديث w و b
    w = w - alpha * dw;
    b = b - alpha * db;
end

% رسم خط التكرار رقم 100
h_final = plot(x_plot, w * x_plot + b, 'b-', 'LineWidth', 2.5, 'DisplayName', 'Iter 100');

% رسم الخط المثالي (polyfit)
h_opt = plot(x_plot, y_opt, 'k--', 'LineWidth', 2.5, 'DisplayName', sprintf('Optimal Line (y = %.2fx + %.2f)', p_opt(1), p_opt(2)));

% رسم النقاط الأصلية
h_data = plot(x, y, 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'r', 'DisplayName', 'Data Points');

title(sprintf('تدرج الـ %d تكرار مقارنة بالخط المثالي', epochs));
xlabel('X'); ylabel('Y');
legend([h_data, h_opt, h_final], 'Location', 'northwest');
colormap('cool');
c = colorbar;
c.Label.String = 'Iteration Number (1 to 100)';
clim([1 epochs]);
grid on; axis([0.5 4.5 0 5]);

% --- الرسم الثاني: هبوط الـ MSE وقيمة الخطأ المثالي ---
subplot(1, 2, 2);
optimal_loss = mean((polyval(p_opt, x) - y).^2);
plot(1:epochs, loss_history, 'r-', 'LineWidth', 2, 'DisplayName', 'Gradient Descent MSE'); hold on;
yline(optimal_loss, 'k--', 'LineWidth', 1.5, 'DisplayName', sprintf('Minimum Possible MSE (%.4f)', optimal_loss));
title('هبوط دالة التكلفة (MSE) باتجاه الحد الأدنى');
xlabel('Iteration'); ylabel('MSE Loss');
legend('Location', 'northeast');
grid on;

% طباعة النتائج في الكونسول للمقارنة
fprintf('--- مقارنة النتائج بعد %d تكرار ---\n', epochs);
fprintf('القيم بالتكرار اليدوي:   w = %.4f | b = %.4f | MSE = %.4f\n', w, b, loss_history(end));
fprintf('القيم بالحل المثالي:     w = %.4f | b = %.4f | MSE = %.4f\n', p_opt(1), p_opt(2), optimal_loss);