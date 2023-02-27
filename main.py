from sampler import NormalSampler
from variance import VarianceCollection
import variance as var
from graph import BoxPlot

MEAN = 170
STD = 10

if __name__ == "__main__":
    # 分散, 不偏分散ともにサンプルサイズの増加につれ母分散に収束することを確認
    variance_plot = BoxPlot("Variance")
    unbiased_variance_plot = BoxPlot("Unbiased Variance")

    for sample_size in range(10, 210, 10):
        sampler = NormalSampler(MEAN, STD, sample_size)

        variance = var.CreateVarianceCollection()
        unbiased_variance = var.CreateUnbiasedVarianceCollection()
        for sample_id in range(100):
            sample = sampler.get()
            variance.append(sample)
            unbiased_variance.append(sample)

        variance_plot.add_plot(variance.get(), f"{sample_size}")
        unbiased_variance_plot.add_plot(unbiased_variance.get(),
                                        f"{sample_size}")

    variance_plot.draw()
    unbiased_variance_plot.draw()

    # サンプルサイズが小さいうちは不偏分散が有利であることを確認
    compare_plot = BoxPlot("Compare Variance UnbiasedVariance")
    for sample_size in range(10, 60, 10):
        sampler = NormalSampler(MEAN, STD, sample_size)

        variance = var.CreateVarianceCollection()
        unbiased_variance = var.CreateUnbiasedVarianceCollection()
        for sample_id in range(1000):
            sample = sampler.get()
            variance.append(sample)
            unbiased_variance.append(sample)

        compare_plot.add_plot(variance.get(), f"V:{sample_size}")
        compare_plot.add_plot(unbiased_variance.get(), f"U:{sample_size}")

    compare_plot.draw()
