# LLC/SNAP ARP decoder bounds check

The initial receive check covers Ethernet and the fixed ARP fields. Optional encapsulation changes where the ARP fields begin, so the decoder must check the captured length again before reading them.

```mermaid
flowchart TD
    A[Use the captured length, not the wire length] --> B{Base frame fits?}
    B -->|No| R[Reject as truncated]
    B -->|Yes| C[Inspect Ethernet and optional VLAN framing]
    C --> D{LLC/SNAP detected?}
    D -->|No| E[Decode the bounded ARP fields]
    D -.->|Before the fix| F[Skip LLC/SNAP without checking the remaining bytes]
    F --> G[ARP field reads can exceed the captured buffer]
    D -->|With the fix| H{LLC/SNAP header and full ARP payload fit?}
    H -->|No| R
    H -->|Yes| I[Skip LLC/SNAP]
    I --> E
```

AddressSanitizer confirmed the out-of-bounds read in a direct parser test before the fix. Live-network behavior was not verified. This page documents the fix; adding it does not change the decoder.
