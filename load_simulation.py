graph TD
    A[Bad Configuration / Update Deployed] --> B{Automated Health Checks}
    B -->|Checks Fail| C[Servers Marked Unhealthy & Dropped]
    C --> D[Remaining Servers Absorb 100% Traffic]
    D --> E[Severe CPU & Memory Overload]
    E --> F[Cascading Regional Outage: Outlook, Teams, M365]
    F --> G[Recovery Phase: Traffic Throttling & Node Restarts]
    
    style A fill:#ffcccc,stroke:#cc0000,stroke-width:2px
    style F fill:#ff9999,stroke:#990000,stroke-width:2px
    style G fill:#ccffcc,stroke:#009900,stroke-width:2px
