# AVA+RSU — Neuroplasticidad Visual Antideepfake (v1.0)

**Objetivo.** Entrenar y evaluar detección humana de deepfakes mientras se respeta un presupuesto de exposición visual saludable cuantificado en **RSU (Retinal Stress Units)**.

**Diseño.** Doble ciego con bloques de estímulos (real vs. sintético), control de luminancia (cd/m²), frecuencia de parpadeo, distancia, y tiempos on/off. Biomarcadores ligeros: pupila (webcam/eye‑tracker), tasa de parpadeo, micro‑sacadas; opcional EEG/EMG.

**RSU (definición operativa).** RSU es una función compuesta de carga visual por unidad de tiempo que integra luminancia efectiva, tiempo de fijación continua, supresión de parpadeo, tamaño pupilar normalizado y densidad de micro‑sacadas. Ver `src/rsu/rsu.py` para la fórmula paramétrica y factores de ponderación.

**Métrica primaria.** AUC de detección bajo tope de RSU por sesión; secundaria: estabilidad pupilar y tiempo‑a‑fatiga.

**Ética.** Consentimiento informado, pausas obligatorias, límites de RSU por sesión/día, y derivación clínica si hay signos de astenopia severa.
