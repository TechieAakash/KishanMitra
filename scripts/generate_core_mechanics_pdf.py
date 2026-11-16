"""
Generate KisanMitra Technical Architecture & AI Core Mechanics PDF.
Contains:
1. Executive Overview & Problem Context
2. Hybrid Tri-Model Machine Learning Architecture
   - Fuzzy Logic Agronomic Expert
   - Gaussian Naive Bayes Likelihood Expert
   - Decision Tree Partitioning Expert
   - Tri-Model Ensemble Synthesis & Dynamic Weighting
3. Agricultural RAG (Retrieval-Augmented Generation)
   - Knowledge Base & Vector Indexing (ChromaDB)
   - Hybrid Retrieval Engine (Dense Semantic + Lexical Matching)
   - Google Gemini API Integration & Prompt Engineering
   - 3-Tier Multi-Level Failover & Grounded Citations
4. Full Stack System Architecture & Real-Time Flow
   - FastAPI Backend & Database Management
   - React 18 + TypeScript Frontend & State Management
   - Vite Watcher & SQLite WAL Concurrency Optimization
5. Complete Farmer User Journey Walkthrough
"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

PDF_OUTPUT_PATH = os.path.join(os.getcwd(), "docs", "project_viva", "KisanMitra_Core_AI_and_Feature_Mechanics.pdf")

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        if self._pageNumber == 1:
            return  # Suppress headers/footers on cover page
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#555555"))
        
        # Header
        self.drawString(54, letter[1] - 36, "KisanMitra: Technical Architecture, ML Ensemble & Agricultural RAG Mechanics")
        self.setStrokeColor(colors.HexColor("#D1D5DB"))
        self.setLineWidth(0.5)
        self.line(54, letter[1] - 42, letter[0] - 54, letter[1] - 42)
        
        # Footer
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(letter[0] - 54, 36, page_text)
        self.drawString(54, 36, "Confidential - For Academic Evaluation & Technical Viva")
        self.setStrokeColor(colors.HexColor("#D1D5DB"))
        self.setLineWidth(0.5)
        self.line(54, 46, letter[0] - 54, 46)
        self.restoreState()

def build_pdf():
    doc = SimpleDocTemplate(
        PDF_OUTPUT_PATH,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom styles
    c_forest = colors.HexColor("#174B35")
    c_saffron = colors.HexColor("#D97706")
    c_dark = colors.HexColor("#1F2937")
    c_gray_bg = colors.HexColor("#F9FAFB")
    c_border = colors.HexColor("#E5E7EB")

    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=c_forest,
        alignment=1,
        spaceAfter=12
    )

    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#4B5563"),
        alignment=1,
        spaceAfter=20
    )

    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=c_forest,
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=c_saffron,
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    h3_style = ParagraphStyle(
        'H3',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=c_dark,
        spaceBefore=6,
        spaceAfter=2,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=c_dark,
        spaceAfter=6
    )

    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#065F46"),
        backColor=colors.HexColor("#ECFDF5"),
        spaceBefore=4,
        spaceAfter=6
    )

    callout_style = ParagraphStyle(
        'Callout',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=12.5,
        textColor=colors.HexColor("#374151")
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=c_dark
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white
    )

    story = []

    # ==================== COVER PAGE ====================
    story.append(Spacer(1, 40))
    story.append(Paragraph("KISANMITRA: DECISION INTELLIGENCE PLATFORM", title_style))
    story.append(Paragraph("Comprehensive Technical Reference Manual: Core AI Mechanics, Hybrid ML Ensemble, Vector RAG & Gemini Architecture", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=c_saffron, spaceAfter=25))

    meta_table_data = [
        [Paragraph("<b>Document Scope</b>", table_cell), Paragraph("In-Depth Algorithmic & System Mechanics Explanation", table_cell)],
        [Paragraph("<b>Core Modules Covered</b>", table_cell), Paragraph("Fuzzy Logic, Gaussian Naive Bayes, Decision Trees, Ensemble, Vector RAG, Gemini API, SQLite WAL Concurrency", table_cell)],
        [Paragraph("<b>Target Audience</b>", table_cell), Paragraph("Technical Viva Evaluators, Software Architects, Academic Panels", table_cell)],
        [Paragraph("<b>Target Geography</b>", table_cell), Paragraph("Uttarakhand Agro-Climatic Pilot (Mid-Hills & Valleys)", table_cell)],
        [Paragraph("<b>Version / Status</b>", table_cell), Paragraph("Release v1.2 — Architecture Audited & Operational", table_cell)],
    ]
    meta_table = Table(meta_table_data, colWidths=[150, 350])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), c_gray_bg),
        ('BOX', (0, 0), (-1, -1), 1, c_border),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, c_border),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 30))

    exec_summary_box = [
        [Paragraph("<b>EXECUTIVE SUMMARY & ARCHITECTURAL INTENT</b><br/><br/>"
                   "KisanMitra is an evidence-grounded agronomic decision-support platform engineered to solve agricultural advice fragility. "
                   "Traditional agricultural advisory tools suffer from two critical flaws: generic machine learning models that generate recommendations disconnected from local agronomic physiology, "
                   "and LLMs that hallucinate unsubstantiated fertilizer and chemical recommendations. "
                   "KisanMitra resolves this by deploying a calibrated <b>Tri-Model Machine Learning Ensemble</b> alongside an <b>Evidence-Grounded Retrieval-Augmented Generation (RAG)</b> knowledge pipeline powered by verified research from GBPUAT Pantnagar and ICAR-VPKAS Almora.", callout_style)]
    ]
    exec_table = Table(exec_summary_box, colWidths=[504])
    exec_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#EFF6FF")),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#93C5FD")),
        ('PADDING', (0, 0), (-1, -1), 12),
    ]))
    story.append(exec_table)

    story.append(PageBreak())

    # ==================== SECTION 1: HYBRID ML ENGINE ====================
    story.append(Paragraph("1. The Hybrid Tri-Model Crop Recommendation Architecture", h1_style))
    story.append(Paragraph(
        "The crop recommendation engine evaluates a 7-dimensional agronomic vector for each farm: "
        "<b>Nitrogen (N), Phosphorus (P), Potassium (K), Temperature (°C), Relative Humidity (%), Soil pH, and Rainfall (mm)</b>. "
        "To achieve maximum reliability across 22 crop classes, KisanMitra does not rely on a single model. "
        "Instead, it combines three distinct paradigms: continuous membership modeling (Fuzzy Logic), multivariate likelihood density estimation (Gaussian Naive Bayes), and deterministic boundary partitioning (Decision Tree).",
        body_style
    ))

    story.append(Paragraph("A. Expert 1: Agronomic Fuzzy Logic Classifier", h2_style))
    story.append(Paragraph(
        "<b>Why Fuzzy Logic?</b> Biological systems do not operate with rigid step functions. If a crop optimally thrives at pH 6.0 to 7.0, an observed pH of 5.92 should not drop the compatibility to zero. "
        "Fuzzy Logic models continuous degrees of membership μ ∈ [0, 1].",
        body_style
    ))
    story.append(Paragraph(
        "<b>Mathematical Formulation:</b><br/>"
        "1. <b>Observed Compatibility Plateau:</b> The training split quantiles [Q15, Q85] define the region of full empirical suitability where μ = 1.0.<br/>"
        "2. <b>Gaussian Roll-off:</b> Outside the plateau, compatibility decays exponentially according to standard deviation σ:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;For x < Q15: μ(x) = exp(-0.5 * ((Q15 - x) / (1.5 * σ))²)<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;For x > Q85: μ(x) = exp(-0.5 * ((x - Q85) / (1.5 * σ))²)<br/>"
        "3. <b>Weighted Geometric Mean (Fuzzy T-Norm Product):</b> The 7 features are aggregated into an overall suitability score using domain importance weights (Rainfall: 1.3, Temperature: 1.2, pH: 1.1, Humidity: 1.1, N-P-K: 1.0):<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Suitability(c) = exp( Σ (w_j * ln(μ_j)) / Σ w_j )<br/>"
        "4. <b>Normalization:</b> Normalized across all 22 candidate classes to produce a valid probability-like distribution.",
        body_style
    ))

    story.append(Spacer(1, 4))
    story.append(Paragraph("B. Expert 2: Gaussian Naive Bayes Likelihood Estimator", h2_style))
    story.append(Paragraph(
        "<b>Statistical Probability Modeling:</b> GaussianNB evaluates conditional probability density using Bayes' Rule under the assumption of feature normality within each crop cluster:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;P(Crop c | x) = [ P(Crop c) * ∏ P(x_j | Crop c) ] / P(x)<br/>"
        "Where each conditional likelihood is calculated via the normal probability density function:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;P(x_j | Crop c) = (1 / √(2π σ²_c,j)) * exp( -(x_j - μ_c,j)² / (2 σ²_c,j) )",
        body_style
    ))
    story.append(Paragraph(
        "<b>Variance Smoothing Optimization:</b> When historical feature variance is very low, the Gaussian denominator approaches zero, leading to extreme probability spikes. "
        "KisanMitra tunes the <code>var_smoothing</code> parameter across 25 log-spaced candidates (10⁻¹¹ to 10⁻¹) using 5-Fold Stratified Cross-Validation on the training partition, guaranteeing robust probability calibration.",
        body_style
    ))

    story.append(Spacer(1, 4))
    story.append(Paragraph("C. Expert 3: Decision Tree Partitioning Classifier", h2_style))
    story.append(Paragraph(
        "<b>Deterministic Boundary Verification:</b> The Decision Tree partitions the 7D space using orthogonal hyperplanes based on Gini impurity reduction:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;I_G(t) = 1 - Σ p(i | t)²<br/>"
        "It acts as a hard agronomic guardrail. For example, if a cold-climate crop requires temperatures below 22°C or high potassium levels, the Decision Tree establishes strict cutoffs that prevent unsuitable recommendations from surviving even if probabilistic density is noisy.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Hyperparameter Regularization:</b> Tuned using 5-Fold Stratified CV across <code>max_depth</code> (6–15), <code>min_samples_split</code> (2–10), and <code>min_samples_leaf</code> (1–4) to prevent overfitting.",
        body_style
    ))

    story.append(Spacer(1, 4))
    story.append(Paragraph("D. Tri-Model Ensemble Synthesis & Consensus Logic", h2_style))
    story.append(Paragraph(
        "The runtime ensemble aggregates predictions using calibrated discriminative weights:<br/>"
        "<b>Ensemble Score = (W_Fuzzy * S_Fuzzy) + (W_GNB * P_GNB) + (W_DT * P_DT)</b><br/>"
        "Calibrated Weights: GaussianNB = <b>0.62</b>, Decision Tree = <b>0.38</b>, Fuzzy Logic = <b>0.00 (active qualitative boundary validator & XAI engine)</b>.<br/>"
        "When all three models pick the same top crop, the system marks the prediction as <b>'Unanimous (3/3 Experts) Consensus'</b>.",
        body_style
    ))

    model_comp_data = [
        [Paragraph("<b>Model Name</b>", table_header), Paragraph("<b>Paradigm</b>", table_header), Paragraph("<b>Key Strength</b>", table_header), Paragraph("<b>Role in KisanMitra</b>", table_header)],
        [Paragraph("<b>Fuzzy Logic Expert</b>", table_cell), Paragraph("Continuous Membership", table_cell), Paragraph("No cliff-edge penalties, human-like domain boundaries", table_cell), Paragraph("Qualitative validator & feature influence XAI radar", table_cell)],
        [Paragraph("<b>Gaussian Naive Bayes</b>", table_cell), Paragraph("Probabilistic Bayes", table_cell), Paragraph("Multivariate density matching on agro-clusters", table_cell), Paragraph("Primary statistical likelihood backbone (62% weight)", table_cell)],
        [Paragraph("<b>Decision Tree</b>", table_cell), Paragraph("Orthogonal Partitioning", table_cell), Paragraph("Strict threshold enforcement & clear decision rules", table_cell), Paragraph("Deterministic environmental safety guardrail (38% weight)", table_cell)],
    ]
    m_table = Table(model_comp_data, colWidths=[110, 110, 140, 144])
    m_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), c_forest),
        ('GRID', (0, 0), (-1, -1), 0.5, c_border),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('PADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(m_table)

    story.append(PageBreak())

    # ==================== SECTION 2: AGRICULTURAL RAG ====================
    story.append(Paragraph("2. Multilingual Agricultural RAG & Gemini Architecture", h1_style))
    story.append(Paragraph(
        "KisanMitra integrates an evidence-grounded Retrieval-Augmented Generation (RAG) assistant designed to completely eliminate LLM hallucination. "
        "Agricultural advice regarding pesticides, seed varieties, and chemical dosages can cause catastrophic crop failure if inaccurate. "
        "Therefore, all conversational advice is grounded strictly in 31 active vector documents from verified research repositories.",
        body_style
    ))

    story.append(Paragraph("A. Document Ingestion, OCR & Vector Storage", h2_style))
    story.append(Paragraph(
        "1. <b>Primary Source Provenance:</b> Official research bulletins published by <b>G.B. Pant University of Agriculture & Technology (GBPUAT) Pantnagar</b> and <b>ICAR-VPKAS Almora</b>.<br/>"
        "2. <b>Multilingual Ingestion & OCR:</b> Historical documents and package-of-practices booklets are ingested using PyMuPDF and Tesseract OCR with dual Devanagari Hindi (<code>hin</code>) and English (<code>eng</code>) traineddata.<br/>"
        "3. <b>Chunking & Dense Vectorization:</b> Documents are chunked with semantic sliding windows (300–500 tokens with 50-token overlap). Embeddings are generated using <code>sentence-transformers/all-MiniLM-L6-v2</code> (384-dimensional dense vectors) and indexed in a persistent <b>ChromaDB</b> vector store.",
        body_style
    ))

    story.append(Paragraph("B. Hybrid Agricultural Retrieval (Dense + Lexical)", h2_style))
    story.append(Paragraph(
        "Pure semantic search often fails with specialized regional crop terminology (e.g., <i>'Jhangora'</i>, <i>'Mandua'</i>, <i>'Khaira disease'</i>). "
        "KisanMitra implements a dual-scoring hybrid retrieval mechanism:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Hybrid Score = (0.65 * Dense Semantic Score) + (0.35 * Lexical BM25 Overlap)</b><br/>"
        "• <b>Dense Search (65%):</b> Cosine similarity between query embedding and chunk vectors.<br/>"
        "• <b>Lexical Search (35%):</b> Language-agnostic token overlap across Devanagari and English keywords.<br/>"
        "• <b>Cutoff Guardrail:</b> Chunks with hybrid similarity < 0.32 are rejected as insufficient evidence to avoid misleading the farmer.",
        body_style
    ))

    story.append(Paragraph("C. Gemini LLM Integration & Prompt Engineering", h2_style))
    story.append(Paragraph(
        "The generation pipeline utilizes Google's official <code>google-genai</code> SDK connecting to <b>Gemini 3.5 Flash Lite</b>:<br/>"
        "• <b>API Security:</b> The <code>GEMINI_API_KEY</code> is loaded securely via environment configuration with sanitization layers ensuring credentials never appear in server logs.<br/>"
        "• <b>Low Temperature Setting:</b> Temperature is pinned to <b>0.2</b> to suppress speculative generation.<br/>"
        "• <b>Temporary Source Identifiers ([S1], [S2]):</b> Evidence chunks are formatted with explicit source tags. The system prompt instructs Gemini:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<i>'Answer strictly based on [S1], [S2]. Cite the exact tag after every dosage or practice. If evidence is missing, state it clearly.'</i><br/>"
        "• <b>Structured Pydantic Output:</b> Gemini produces validated JSON containing the answer, detected language, citation list, and practical follow-up questions.",
        body_style
    ))

    story.append(Paragraph("D. 3-Tier Resilient Fallback System", h2_style))
    story.append(Paragraph(
        "KisanMitra guarantees uninterrupted operation even during internet outages or API quota limits:<br/>"
        "• <b>Tier 1 (Normal Mode):</b> Live Google Gemini synthesis with grounded source citations.<br/>"
        "• <b>Tier 2 (Offline Extraction Fallback):</b> If the Gemini API key is unavailable or quota is exceeded (HTTP 429), the system activates <code>RetrievalOnlyLLMProvider</code>. It delivers verified verbatim excerpts directly from ChromaDB vectors with full citation provenance.<br/>"
        "• <b>Tier 3 (Scope Guardrail):</b> When queries request live data (e.g. <i>'Today's mandi price'</i>), the assistant redirects the farmer to the real-time telemetry dashboards.",
        body_style
    ))

    rag_summary_box = [
        [Paragraph("<b>CORE RAG GUARANTEE: COMPLETE PROVENANCE & ZERO HALLUCINATION</b><br/><br/>"
                   "Every single advisory recommendation displayed on the frontend assistant includes full publisher provenance: "
                   "Document Title, Publishing University, Year of Publication, Page Range, and exact matching snippet text. "
                   "Farmers and researchers can verify every recommendation directly against ICAR and GBPUAT standards.", callout_style)]
    ]
    r_table = Table(rag_summary_box, colWidths=[504])
    r_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#FEF3C7")),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#F59E0B")),
        ('PADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(r_table)

    story.append(PageBreak())

    # ==================== SECTION 3: FULL STACK ARCHITECTURE ====================
    story.append(Paragraph("3. Full-Stack Engineering, Real-Time Flow & Concurrency", h1_style))
    story.append(Paragraph(
        "KisanMitra is built with a high-performance modern software stack separating decision intelligence from frontend presentation.",
        body_style
    ))

    story.append(Paragraph("A. Backend Architecture (FastAPI + SQLAlchemy + SQLite/PostGIS)", h2_style))
    story.append(Paragraph(
        "• <b>FastAPI REST Gateway:</b> High-throughput async framework exposing endpoints for unified crop recommendations, chat assistant, weather telemetry, and mandi economics.<br/>"
        "• <b>Memory Pre-warming:</b> Lifespan context handlers load PyTorch Sentence-Transformers, ChromaDB vectors, and ML models into RAM on server boot, eliminating cold-start request latency.<br/>"
        "• <b>Telemetry Caching:</b> An in-memory cache with 15-minute TTL buffers Open-Meteo weather forecasts and RAG embeddings, slashing API response time from 9+ seconds to under 2 seconds.",
        body_style
    ))

    story.append(Paragraph("B. Database Concurrency & The Vite Watcher Fix", h2_style))
    story.append(Paragraph(
        "<b>The Challenge:</b> During Phase 5 deployment, interacting with <code>/crop-recommendation</code> caused the browser to reload continuously and lag.<br/>"
        "<b>Root Cause Diagnosis:</b> When recommendation requests were processed, FastAPI recorded the request in <code>kisanmitra.db</code>, updating the SQLite write-ahead log (<code>kisanmitra.db-wal</code>). "
        "Vite's default file watcher was monitoring the repository root and mistook the database WAL update for source code changes, repeatedly firing <code>[vite] (client) page reload</code>.<br/>"
        "<b>The Architectural Solution:</b><br/>"
        "1. <b>Vite Configuration:</b> Configured <code>server.watch.ignored</code> in <code>vite.config.ts</code> to ignore all <code>*.db*</code>, <code>*.sqlite3*</code>, and <code>backend/**</code> files.<br/>"
        "2. <b>SQLite WAL & Busy Timeout:</b> Configured <code>PRAGMA journal_mode=WAL</code> and <code>PRAGMA busy_timeout=60000</code> in SQLAlchemy engine hooks, completely eliminating 'database locked' errors during concurrent writes.",
        body_style
    ))

    story.append(Paragraph("C. Frontend Architecture (React 18 + TypeScript + Vite + Tailwind)", h2_style))
    story.append(Paragraph(
        "• <b>Centralized Reactive Context (AppContext):</b> Manages active farm telemetry, user profile, language preferences (Hindi/English), and live recommendation state.<br/>"
        "• <b>Interactive What-If Simulator:</b> Farmers can adjust rainfall and temperature sliders to observe how shifting monsoon patterns dynamically alter crop rankings and model confidence in real-time.<br/>"
        "• <b>Asynchronous Request Debouncing:</b> Added <code>isCalculatingRecommendation</code> state indicators and disabled submit buttons during active pipeline execution to prevent duplicate network calls.",
        body_style
    ))

    story.append(Spacer(1, 6))
    story.append(Paragraph("4. End-to-End Farmer User Flow Summary", h1_style))
    
    flow_steps = [
        [Paragraph("<b>Step 1: Farm Profiling</b>", table_cell), Paragraph("Farmer enters land details (Almora, 1650m elevation, Brown Forest Soil, N-P-K nutrient readings).", table_cell)],
        [Paragraph("<b>Step 2: Unified Synthesis</b>", table_cell), Paragraph("FastAPI integrates soil parameters, live district weather, and APMC market prices.", table_cell)],
        [Paragraph("<b>Step 3: Tri-Model ML Scoring</b>", table_cell), Paragraph("Fuzzy Logic, GaussianNB, and Decision Trees evaluate suitability and compute consensus.", table_cell)],
        [Paragraph("<b>Step 4: RAG Knowledge Binding</b>", table_cell), Paragraph("ChromaDB retrieves GBPUAT/ICAR bulletins; Gemini formats verified practices and citations.", table_cell)],
        [Paragraph("<b>Step 5: Farmer Dashboard Output</b>", table_cell), Paragraph("Farmer views ranked crops, expected yields, mandi profits, What-If simulator, and XAI radar.", table_cell)],
    ]
    flow_table = Table(flow_steps, colWidths=[140, 364])
    flow_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), c_gray_bg),
        ('GRID', (0, 0), (-1, -1), 0.5, c_border),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(flow_table)

    story.append(Spacer(1, 15))
    story.append(HRFlowable(width="100%", thickness=1, color=c_saffron, spaceAfter=10))
    story.append(Paragraph("<para align='center'><b>KisanMitra Technical Manual — Generated Locally for Academic Evaluation</b></para>", subtitle_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF successfully built at: {PDF_OUTPUT_PATH}")

if __name__ == "__main__":
    build_pdf()
