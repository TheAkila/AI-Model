
import { useState } from "react";

const colors = {
  bg: "#0a0e1a",
  cardBg: "#111827",
  cardBorder: "#1e293b",
  gold: "#f0a832",
  goldDim: "#c48a2a",
  teal: "#22d3ee",
  tealDim: "#0e9aad",
  purple: "#a78bfa",
  purpleDim: "#7c5cbf",
  rose: "#fb7185",
  roseDim: "#c4566a",
  green: "#34d399",
  greenDim: "#22a368",
  blue: "#60a5fa",
  blueDim: "#3b7dd8",
  text: "#e2e8f0",
  textDim: "#94a3b8",
  textMuted: "#64748b",
};

const layerData = [
  {
    id: "input",
    label: "DATA INPUT LAYER",
    color: colors.textDim,
    accent: colors.textDim,
    icon: "⬇",
    description: "Raw platform data ingested from Rasaswadaya.lk interactions",
    components: [
      { name: "User Profiles & Behavior", detail: "Browsing, clicks, follows, attendance history" },
      { name: "Artist & Event Metadata", detail: "Genre, region, art form, language, category tags" },
      { name: "Interaction Log", detail: "Likes, shares, follows, event RSVPs, ratings" },
      { name: "Temporal Signals", detail: "Timestamps, seasonal flags, festival markers" },
    ],
  },
  {
    id: "graph",
    label: "SOCIAL GRAPH MINING",
    color: colors.teal,
    accent: colors.tealDim,
    icon: "◈",
    description: "Heterogeneous graph construction and structural feature extraction",
    components: [
      { name: "Graph Construction", detail: "Nodes: Users, Artists, Events, Genres, Locations" },
      { name: "Edge Typing", detail: "Follows, Attends, Performs-at, Belongs-to, Likes" },
      { name: "Community Detection", detail: "Louvain clustering → cultural micro-ecosystems" },
      { name: "Structural Features", detail: "Degree centrality, betweenness, PageRank scores" },
    ],
  },
  {
    id: "dna",
    label: "CULTURAL DNA MAPPING",
    color: colors.gold,
    accent: colors.goldDim,
    icon: "◎",
    description: "Explainable cultural fingerprint vectors assigned to every node",
    components: [
      { name: "Art Form Encoding", detail: "Dance, Music, Drama, Visual, Mixed-media" },
      { name: "Cultural Context", detail: "Traditional, Contemporary, Fusion, Festival-specific" },
      { name: "Regional & Linguistic", detail: "Province-level region + Sinhala/Tamil/English/Mixed" },
      { name: "Mood & Season Vectors", detail: "Celebratory/Reflective + Vesak/New Year/Peradeniya" },
    ],
  },
  {
    id: "gnn",
    label: "GNN CORE ENGINE",
    color: colors.purple,
    accent: colors.purpleDim,
    icon: "⬡",
    description: "The central learning model — fuses graph structure with cultural features",
    components: [
      { name: "Node Initialization", detail: "Cultural DNA vectors as initial node features" },
      { name: "Message Passing (2–3 layers)", detail: "GraphSAGE / GAT aggregation across neighbors" },
      { name: "Attention Mechanism (optional)", detail: "GAT attention weights for explainability" },
      { name: "Embedding Output", detail: "Rich contextual node embeddings for all entities" },
    ],
  },
  {
    id: "temporal",
    label: "TEMPORAL ENHANCEMENT",
    color: colors.rose,
    accent: colors.roseDim,
    icon: "◐",
    description: "Adds time-awareness to static GNN embeddings",
    components: [
      { name: "Time-Windowed Snapshots", detail: "Rolling graph snapshots (weekly/monthly)" },
      { name: "Temporal Edge Features", detail: "Recency weighting on interaction edges" },
      { name: "Trend Velocity Signals", detail: "Rate-of-change in engagement metrics" },
      { name: "Seasonal Pattern Encoder", detail: "Festival & seasonal cycle embeddings" },
    ],
  },
  {
    id: "tasks",
    label: "DOWNSTREAM TASKS",
    color: colors.green,
    accent: colors.greenDim,
    icon: "▶",
    description: "Final predictions and outputs powered by learned embeddings",
    components: [
      { name: "Link Prediction", detail: "Will user attend this event? Follow this artist?" },
      { name: "Trend Detection", detail: "Emerging genres, viral propagation, spike alerts" },
      { name: "Collaboration Scoring", detail: "Artist-Artist compatibility based on graph + culture" },
      { name: "Dashboard Analytics", detail: "Personalized insights for artists & organizers" },
    ],
  },
  {
    id: "explain",
    label: "EXPLAINABILITY LAYER",
    color: colors.blue,
    accent: colors.blueDim,
    icon: "◑",
    description: "Human-readable explanations for every recommendation made",
    components: [
      { name: "GNNExplainer", detail: "Identifies which subgraph caused the prediction" },
      { name: "Attention Weight Readout", detail: "Which neighbors influenced the embedding most" },
      { name: "Cultural DNA Diff", detail: "Shows dimensional similarity breakdown" },
      { name: "User-Facing Reasons", detail: '"Because you attended X" style explanations' },
    ],
  },
];

const flowArrows = [
  { from: "input", to: "graph", label: "Raw data → Graph" },
  { from: "input", to: "dna", label: "Metadata → DNA vectors" },
  { from: "graph", to: "gnn", label: "Graph structure" },
  { from: "dna", to: "gnn", label: "Node features" },
  { from: "gnn", to: "temporal", label: "Static embeddings" },
  { from: "temporal", to: "tasks", label: "Time-aware embeddings" },
  { from: "tasks", to: "explain", label: "Predictions" },
  { from: "dna", to: "explain", label: "Feature refs" },
];

function LayerCard({ layer, expanded, onToggle }) {
  return (
    <div
      style={{
        background: colors.cardBg,
        border: `1px solid ${expanded ? layer.color : colors.cardBorder}`,
        borderRadius: 14,
        overflow: "hidden",
        transition: "all 0.3s ease",
        boxShadow: expanded ? `0 0 24px ${layer.color}22` : "none",
        cursor: "pointer",
      }}
      onClick={onToggle}
    >
      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: 14,
          padding: "16px 20px",
          background: `linear-gradient(90deg, ${layer.color}12, transparent)`,
        }}
      >
        <span style={{ fontSize: 22, color: layer.color }}>{layer.icon}</span>
        <div style={{ flex: 1 }}>
          <div style={{ color: layer.color, fontFamily: "'Courier New', monospace", fontSize: 13, fontWeight: 700, letterSpacing: 2 }}>
            {layer.label}
          </div>
          <div style={{ color: colors.textMuted, fontSize: 12, marginTop: 2 }}>{layer.description}</div>
        </div>
        <span style={{ color: colors.textMuted, fontSize: 18, transition: "transform 0.3s", transform: expanded ? "rotate(180deg)" : "rotate(0deg)" }}>▼</span>
      </div>

      {expanded && (
        <div style={{ padding: "0 20px 18px", display: "grid", gridTemplateColumns: "1fr 1fr", gap: 10 }}>
          {layer.components.map((c, i) => (
            <div
              key={i}
              style={{
                background: `${layer.color}08`,
                border: `1px solid ${layer.color}25`,
                borderRadius: 8,
                padding: "10px 14px",
              }}
            >
              <div style={{ color: layer.color, fontSize: 13, fontWeight: 600 }}>{c.name}</div>
              <div style={{ color: colors.textMuted, fontSize: 11.5, marginTop: 3 }}>{c.detail}</div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

function FlowConnector({ color, label }) {
  return (
    <div style={{ display: "flex", alignItems: "center", justifyContent: "center", padding: "4px 0" }}>
      <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
        <div style={{ width: 2, height: 22, background: `linear-gradient(to bottom, ${color}, ${color}66)` }} />
        <span style={{ color: color, fontSize: 10, fontFamily: "'Courier New', monospace", opacity: 0.7, letterSpacing: 1 }}>{label}</span>
      </div>
    </div>
  );
}

function LimitationCard({ title, severity, description, solution }) {
  const sevColors = { high: colors.rose, medium: colors.gold, low: colors.green };
  const sevLabels = { high: "CRITICAL", medium: "IMPORTANT", low: "MINOR" };
  return (
    <div style={{ background: colors.cardBg, border: `1px solid ${sevColors[severity]}33`, borderRadius: 10, padding: "14px 18px" }}>
      <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 6 }}>
        <span style={{ background: sevColors[severity], color: "#0a0e1a", fontSize: 10, fontWeight: 700, padding: "2px 8px", borderRadius: 4, letterSpacing: 1 }}>
          {sevLabels[severity]}
        </span>
        <span style={{ color: colors.text, fontSize: 13, fontWeight: 600 }}>{title}</span>
      </div>
      <p style={{ color: colors.textMuted, fontSize: 12, margin: 0, lineHeight: 1.5 }}>{description}</p>
      <p style={{ color: sevColors[severity], fontSize: 12, margin: "6px 0 0", fontWeight: 600 }}>✓ Fix: {solution}</p>
    </div>
  );
}

function ComparisonRow({ aspect, gnnOnly, fullModel }) {
  return (
    <tr style={{ borderBottom: `1px solid ${colors.cardBorder}` }}>
      <td style={{ padding: "10px 14px", color: colors.gold, fontSize: 13, fontWeight: 600 }}>{aspect}</td>
      <td style={{ padding: "10px 14px", color: colors.roseDim, fontSize: 12 }}>{gnnOnly}</td>
      <td style={{ padding: "10px 14px", color: colors.green, fontSize: 12 }}>{fullModel}</td>
    </tr>
  );
}

export default function RasaswadayaArchitecture() {
  const [expandedLayers, setExpandedLayers] = useState({ gnn: true, dna: true });
  const [activeTab, setActiveTab] = useState("architecture");

  const toggleLayer = (id) => {
    setExpandedLayers((prev) => ({ ...prev, [id]: !prev[id] }));
  };

  const tabs = [
    { id: "architecture", label: "◈ Architecture" },
    { id: "limitations", label: "⚠ GNN Limitations" },
    { id: "comparison", label: "≡ GNN-Only vs Full" },
  ];

  const limitations = [
    { title: "No Temporal Awareness", severity: "high", description: "Standard GNNs see a static graph snapshot. Trends, seasonal patterns, and evolving user preferences are completely invisible.", solution: "Layer temporal edge features + time-windowed graph snapshots on top of the GNN." },
    { title: "Cold-Start Failure", severity: "high", description: "New artists/events with zero edges produce meaningless embeddings. The GNN has no signal to learn from for isolated nodes.", solution: "Cultural DNA vectors provide meaningful features from day one, before any graph edges exist." },
    { title: "Sparse Graph Overfitting", severity: "high", description: "Pre-launch or early-stage platforms have very few interactions. GNNs will overfit quickly on sparse graphs.", solution: "Graph augmentation (edge dropout, feature masking) + strong regularization + careful train/val splits." },
    { title: "Black-Box Embeddings", severity: "medium", description: "GNN-learned embeddings are dense vectors with no inherent human meaning. Academic reviewers and users expect explainability.", solution: "Use GAT attention weights + GNNExplainer + Cultural DNA dimension-level similarity readouts." },
    { title: "No Semantic Content Understanding", severity: "medium", description: "GNNs model graph structure, not content semantics. Two artists with similar lyrics but no shared edges look unrelated.", solution: "Feed Cultural DNA vectors (encoding art form, mood, style) as node features into the GNN input layer." },
    { title: "Scalability Ceiling", severity: "low", description: "Full-batch GNN training on very large graphs is memory-intensive. Not a concern now, but worth noting for future.", solution: "GraphSAGE uses mini-batch sampling — scales well. Stay with sampled aggregation from the start." },
  ];

  const comparisons = [
    { aspect: "Recommendation Quality", gnnOnly: "Moderate — misses temporal and semantic signals", fullModel: "High — fuses structure + culture + time" },
    { aspect: "Cold-Start Handling", gnnOnly: "Fails completely for new nodes", fullModel: "Cultural DNA provides baseline features" },
    { aspect: "Trend Detection", gnnOnly: "Cannot detect — no time awareness", fullModel: "Temporal layer captures emerging trends" },
    { aspect: "Explainability", gnnOnly: "Black box — hard to justify to reviewers", fullModel: "Cultural DNA diffs + attention weights explain why" },
    { aspect: "Seasonal Awareness", gnnOnly: "Vesak, New Year invisible to model", fullModel: "Seasonal encoder captures festival cycles" },
    { aspect: "Academic Novelty", gnnOnly: "GNN on cultural data — incremental", fullModel: "Cultural DNA + temporal GNN — publishable contribution" },
    { aspect: "Data Efficiency", gnnOnly: "Needs dense interactions to learn well", fullModel: "DNA features compensate for sparse interactions" },
  ];

  return (
    <div style={{ background: colors.bg, minHeight: "100vh", color: colors.text, fontFamily: "'Segoe UI', system-ui, sans-serif", padding: "32px 24px" }}>
      {/* Header */}
      <div style={{ textAlign: "center", marginBottom: 32 }}>
        <div style={{ display: "inline-flex", alignItems: "center", gap: 10, background: `${colors.gold}10`, border: `1px solid ${colors.gold}33`, borderRadius: 24, padding: "6px 18px", marginBottom: 16 }}>
          <span style={{ color: colors.gold, fontSize: 14 }}>◎</span>
          <span style={{ color: colors.gold, fontSize: 12, fontFamily: "'Courier New', monospace", letterSpacing: 2 }}>RASASWADAYA.LK</span>
        </div>
        <h1 style={{ margin: 0, fontSize: 26, fontWeight: 700, background: `linear-gradient(135deg, ${colors.teal}, ${colors.purple}, ${colors.gold})`, WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent" }}>
          GNN-Based AI Model Architecture
        </h1>
        <p style={{ color: colors.textMuted, fontSize: 13, marginTop: 8 }}>Social Graph Mining · Cultural DNA Mapping · Graph Neural Networks</p>
      </div>

      {/* Tabs */}
      <div style={{ display: "flex", justifyContent: "center", gap: 8, marginBottom: 28 }}>
        {tabs.map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            style={{
              background: activeTab === tab.id ? `${colors.purple}18` : "transparent",
              border: `1px solid ${activeTab === tab.id ? colors.purple : colors.cardBorder}`,
              color: activeTab === tab.id ? colors.purple : colors.textMuted,
              borderRadius: 20,
              padding: "7px 18px",
              fontSize: 13,
              cursor: "pointer",
              fontFamily: "'Courier New', monospace",
              letterSpacing: 0.5,
              transition: "all 0.2s",
            }}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* Architecture Tab */}
      {activeTab === "architecture" && (
        <div style={{ maxWidth: 680, margin: "0 auto" }}>
          <p style={{ color: colors.textMuted, fontSize: 12, textAlign: "center", marginBottom: 20, fontStyle: "italic" }}>
            Click each layer to expand components · GNN Core + Cultural DNA are expanded by default
          </p>
          {layerData.map((layer, i) => (
            <div key={layer.id}>
              <LayerCard layer={layer} expanded={!!expandedLayers[layer.id]} onToggle={() => toggleLayer(layer.id)} />
              {i < layerData.length - 1 && (
                <FlowConnector
                  color={i === 0 ? colors.teal : i === 1 ? colors.gold : i === 2 ? colors.purple : i === 3 ? colors.rose : colors.green}
                  label={flowArrows[i]?.label || "▼"}
                />
              )}
            </div>
          ))}

          {/* Legend */}
          <div style={{ marginTop: 28, background: colors.cardBg, border: `1px solid ${colors.cardBorder}`, borderRadius: 12, padding: "16px 20px" }}>
            <div style={{ color: colors.textMuted, fontSize: 11, fontFamily: "'Courier New', monospace", letterSpacing: 1, marginBottom: 10 }}>LAYER ROLES</div>
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "6px 20px" }}>
              {[
                { color: colors.textDim, label: "Data Input", role: "Raw material" },
                { color: colors.teal, label: "Graph Mining", role: "Structure extraction" },
                { color: colors.gold, label: "Cultural DNA", role: "Semantic features" },
                { color: colors.purple, label: "GNN Core", role: "Learning engine" },
                { color: colors.rose, label: "Temporal", role: "Time awareness" },
                { color: colors.green, label: "Downstream", role: "Predictions" },
                { color: colors.blue, label: "Explainability", role: "Human-readable" },
              ].map((item, i) => (
                <div key={i} style={{ display: "flex", alignItems: "center", gap: 8 }}>
                  <div style={{ width: 10, height: 10, borderRadius: "50%", background: item.color }} />
                  <span style={{ color: colors.text, fontSize: 12 }}>{item.label}</span>
                  <span style={{ color: colors.textMuted, fontSize: 11 }}>— {item.role}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* Limitations Tab */}
      {activeTab === "limitations" && (
        <div style={{ maxWidth: 680, margin: "0 auto" }}>
          <p style={{ color: colors.textMuted, fontSize: 13, textAlign: "center", marginBottom: 22 }}>
            6 known limitations of using GNNs alone — each has a concrete solution built into the full architecture
          </p>
          <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
            {limitations.map((l, i) => (
              <LimitationCard key={i} {...l} />
            ))}
          </div>
        </div>
      )}

      {/* Comparison Tab */}
      {activeTab === "comparison" && (
        <div style={{ maxWidth: 720, margin: "0 auto" }}>
          <p style={{ color: colors.textMuted, fontSize: 13, textAlign: "center", marginBottom: 22 }}>
            Why the full layered model outperforms a GNN-only approach across every dimension
          </p>
          <div style={{ background: colors.cardBg, border: `1px solid ${colors.cardBorder}`, borderRadius: 14, overflow: "hidden" }}>
            <table style={{ width: "100%", borderCollapse: "collapse" }}>
              <thead>
                <tr style={{ background: `${colors.cardBg}` }}>
                  <th style={{ padding: "12px 14px", textAlign: "left", color: colors.gold, fontSize: 12, fontFamily: "'Courier New', monospace", letterSpacing: 1, borderBottom: `2px solid ${colors.cardBorder}` }}>ASPECT</th>
                  <th style={{ padding: "12px 14px", textAlign: "left", color: colors.rose, fontSize: 12, fontFamily: "'Courier New', monospace", letterSpacing: 1, borderBottom: `2px solid ${colors.cardBorder}` }}>✗ GNN ONLY</th>
                  <th style={{ padding: "12px 14px", textAlign: "left", color: colors.green, fontSize: 12, fontFamily: "'Courier New', monospace", letterSpacing: 1, borderBottom: `2px solid ${colors.cardBorder}` }}>✓ FULL MODEL</th>
                </tr>
              </thead>
              <tbody>
                {comparisons.map((c, i) => (
                  <ComparisonRow key={i} {...c} />
                ))}
              </tbody>
            </table>
          </div>

          {/* Verdict box */}
          <div style={{ marginTop: 20, background: `${colors.green}0a`, border: `1px solid ${colors.green}33`, borderRadius: 12, padding: "18px 22px" }}>
            <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 8 }}>
              <span style={{ color: colors.green, fontSize: 16 }}>◎</span>
              <span style={{ color: colors.green, fontWeight: 700, fontSize: 14 }}>VERDICT</span>
            </div>
            <p style={{ color: colors.text, fontSize: 13, margin: 0, lineHeight: 1.6 }}>
              GNN is the <strong style={{ color: colors.purple }}>core engine</strong> — it's the right choice for learning from graph-structured cultural data. But it must be <strong style={{ color: colors.gold }}>wrapped with Cultural DNA Mapping</strong> for semantic grounding, <strong style={{ color: colors.rose }}>Temporal Enhancement</strong> for trend awareness, and <strong style={{ color: colors.blue }}>Explainability tools</strong> for academic credibility. The full layered architecture is your thesis contribution.
            </p>
          </div>
        </div>
      )}

      {/* Footer */}
      <div style={{ textAlign: "center", marginTop: 36, color: colors.textMuted, fontSize: 11, fontFamily: "'Courier New', monospace" }}>
        RASASWADAYA.LK · AI MODEL ARCHITECTURE · ACADEMIC RESEARCH
      </div>
    </div>
  );
}
