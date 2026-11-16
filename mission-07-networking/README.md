# Mission 7 — How Computers Communicate

---

## 1. Task / Objective
The objective of Mission 7 was to demystify computer networking principles and investigate how devices communicate across local and global networks. This included:
1. Defining and providing real-world examples for eight essential networking concepts: LAN, MAN, WAN, DNS, Router, Protocol, Packet Switching, and Client-Server Architecture.
2. Performing live, privacy-safe network diagnostic tests using Terminal (`ping` and `nslookup`) against a public example domain (`example.com`).
3. Formulating a step-by-step technical explanation (5–7 steps) detailing exactly what occurs when a user enters a website URL into a web browser.

---

## 2. Work Completed
- **Networking Concepts Framework**: Completed the core conceptual table defining network scale, addressing, routing, protocols, and architectural models with tangible examples.
- **Network Diagnostics Executed**:
  - Performed ICMP connectivity test with `ping -c 3 example.com`, verifying end-to-end latency (average round-trip time: ~9.7 ms, 0.0% packet loss).
  - Queried public DNS records using `nslookup example.com`, observing address resolution to IP addresses (`172.66.147.243` and `104.20.23.154`).
- **End-to-End Web Lifecycle**: Documented a comprehensive 6-step breakdown of web browsing, accurately utilizing the terms *client*, *server*, *DNS*, and *protocol*.
- **Privacy Protection**: Redacted local LAN addresses and Wi-Fi SSID details to maintain complete personal privacy.
- **Viva Preparation**: Prepared 5 teacher explanation questions and answers exploring IP addressing, packet routing, and HTTP/HTTPS.

---

## 3. Commands / Tools Used

| Tool / Command | Category | Purpose |
| :--- | :--- | :--- |
| `ping -c 3 <host>` | Connectivity Test | Sends ICMP Echo Request packets to check network reachability and measure round-trip response latency. |
| `nslookup <domain>` | Name Resolution | Queries a Domain Name System (DNS) server to find the IP address mapped to a domain name. |
| `dig <domain>` | DNS Inspection | Advanced DNS lookup utility displaying query times, authoritative answers, and record flags. |

---

## 4. My Understanding

### Task 7.1 — Network Concepts Table

| Concept | Explain It in Your Own Words | Real-World Example |
| :--- | :--- | :--- |
| **LAN (Local Area Network)** | A high-speed network that interconnects computers and devices within a limited geographical area such as a single home, classroom, or office building. | The Wi-Fi network in my house connecting my laptop, phone, and home printer. |
| **MAN (Metropolitan Area Network)** | A network that spans an entire town, city, or large university campus, larger than a LAN but smaller than a global WAN. | A municipal cable television network or an interconnected smart-city traffic monitoring grid spanning Bengaluru. |
| **WAN (Wide Area Network)** | A massive telecommunications network that spans vast geographical distances across states, countries, or the entire globe. | **The Internet** itself, connecting millions of private, corporate, and educational networks worldwide via undersea fiber-optic cables. |
| **DNS (Domain Name System)** | The "phonebook" of the Internet; translates human-memorable domain names (like `google.com`) into computer-readable numerical IP addresses (like `142.250.190.46`). | When you type `example.com`, DNS servers look up which server IP hosts that domain. |
| **Router** | A specialized networking hardware device that directs data packets between different networks, deciding the best physical path for each packet. | The home Wi-Fi broadband router that connects my local home devices to the Internet Service Provider's (ISP) network. |
| **Protocol** | An agreed-upon set of rules, formats, and conventions that define how electronic devices format, transmit, verify, and acknowledge data. | **HTTP/HTTPS** for transferring web pages; **TCP/IP** for reliable packet transmission. |
| **Packet Switching** | A data transmission method where digital messages are sliced into small chunks called "packets", sent independently across various network paths, and reassembled at the destination. | Streaming a YouTube video where millions of small data packets take different routes across the internet and are reordered seamlessly by your player. |
| **Client-Server** | A distributed computing architecture where a requesting program (**client**) asks for data or services, and a centralized host machine (**server**) processes the request and serves the response. | Google Chrome running on my laptop (the **client**) requesting web pages from a remote web server (the **server**). |

---

### Task 7.2 — Live Network Diagnostics (Privacy-Safe)

#### 1. Connectivity Test Output (`ping -c 3 example.com`)
```text
PING example.com (104.20.23.154): 56 data bytes
64 bytes from 104.20.23.154: icmp_seq=0 ttl=58 time=6.176 ms
64 bytes from 104.20.23.154: icmp_seq=1 ttl=58 time=6.669 ms
64 bytes from 104.20.23.154: icmp_seq=2 ttl=58 time=16.258 ms

--- example.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 6.176/9.701/16.258/4.641 ms
```

#### 2. DNS Lookup Output (`nslookup example.com`)
```text
Server:		8.8.8.8
Address:	8.8.8.8#53

Non-authoritative answer:
Name:	example.com
Address: 172.66.147.243
Name:	example.com
Address: 104.20.23.154
```

#### Answers to Diagnostic Questions:

1. **What does a connectivity test (`ping`) help you check?**
   - It verifies whether your computer has an active physical and logical route to a remote host. It measures packet transmission loss (0% loss indicates a stable connection) and calculates the **round-trip time (latency)** in milliseconds.

2. **What information does a DNS lookup display?**
   - It displays the resolver server handling the query (e.g. Google Public DNS `8.8.8.8` on port `53`) and the corresponding **A Records** (IPv4 addresses) or **AAAA Records** (IPv6 addresses) associated with that domain name.

3. **What is the role of DNS when you enter a website name in a browser?**
   - Browsers cannot communicate using human text like `github.com`; networking hardware only understands numerical IP addresses. DNS acts as an automated directory service that resolves the domain name into an IP address in milliseconds so the browser knows which exact server to connect to.

---

### Task 7.3 — What Happens When You Open a Website? (6-Step Lifecycle)

Here is the technical sequence of events when a user navigates to a website:

1. **Step 1: User Input & Local Cache Check (Client)**
   The user enters a URL (e.g. `https://example.com`) into their web browser (the **client**). The browser checks its local browser cache, operating system cache, and router cache to see if the corresponding IP address was recently looked up.

2. **Step 2: DNS Resolution (DNS)**
   If the IP address is not cached, the client dispatches a DNS query to a recursive DNS resolver (provided by the ISP or configured services like `8.8.8.8`). The resolver queries Root, TLD (.com), and Authoritative nameservers, translating `example.com` into its destination IP address (`104.20.23.154`).

3. **Step 3: Establishing the Connection (TCP & TLS Protocols)**
   Using the resolved IP address, the client initiates a connection to the destination **server**. The devices perform a **TCP 3-Way Handshake** (SYN, SYN-ACK, ACK) to ensure reliable communication. For secure HTTPS connections, a **TLS Handshake** follows to authenticate the server's SSL certificate and establish encrypted session keys.

4. **Step 4: Packet Routing Across the Internet (Routers & Packet Switching)**
   The client formats an HTTP `GET` request message. The operating system breaks this request into small digital **packets** according to the TCP/IP protocol suite. Multiple intermediate **routers** forward these packets across fiber-optic cables and networks, dynamically routing around congestion until all packets arrive at the destination server.

5. **Step 5: Server Processing & Response (Server)**
   The web **server** receives and reassembles the incoming packets. The web server software (e.g. Nginx, Apache) processes the request, locates the requested HTML, CSS, JavaScript, and media assets, and packages them into an HTTP Response message (e.g. `200 OK`), which is transmitted back to the client as packets.

6. **Step 6: Client Rendering & Display (Client)**
   The browser receives the response packets, checks for errors, and feeds the HTML document into its rendering engine. The engine builds the Document Object Model (DOM) tree, applies CSS styling, executes JavaScript, and paints the final web page onto the user's screen.

---

## 5. Difficulties Faced
- Understanding the difference between a **router** and a **protocol**: A student might easily confuse the two because both deal with transmitting data.

---

## 6. How I Resolved Them
- Distinguished physical hardware from logical rules: A **router** is a physical hardware machine with physical ports that moves packets across wires. A **protocol** (like HTTP or TCP/IP) is a set of software rules and standards written into code that dictates how those packets must be structured.

---

## 7. Evidence / Files
- `mission-07-networking/README.md`
- Diagnostic command logs: `ping -c 3 example.com` and `nslookup example.com` (All outputs privacy-safe with no private home IP addresses exposed).

---

## 8. Commit Details
- **Commit Message**: `Mission 7: Explain networking concepts and website communication`
- **Target Branch**: `main`
- **Pushed to GitHub**: Yes (Commit pending push confirmation)

---

## How to Explain This Mission to My Teacher

### 1. What was the objective?
"The objective of Mission 7 was to investigate computer networks: defining fundamental network architectures (LAN, WAN, client-server), executing live diagnostic commands (`ping`, `nslookup`), and breaking down the step-by-step lifecycle of loading a web page."

### 2. What practical work did I perform?
"I tested network connectivity by pinging `example.com` to observe round-trip latency and 0% packet loss, queried DNS records using `nslookup` to see domain-to-IP resolution, completed an 8-concept networking table, and wrote a numbered 6-step breakdown of how a web browser retrieves a website."

### 3. Which commands or tools did I use?
"I used `ping` for ICMP connectivity, `nslookup` for DNS name resolution, and Terminal on macOS."

### 4. What did I learn?
"I learned how domain names map to IP addresses via DNS, how data is divided into packets that travel across routers, and how clients and servers exchange HTTP requests and responses using established protocols."

### 5. What was the most important observation?
"The most fascinating observation was seeing `nslookup` resolve `example.com` to real IP addresses (`104.20.23.154`) in just 9 milliseconds, illustrating how fast global DNS resolution operates behind every web click."

### 6. Five Possible Questions My Teacher Might Ask & Simple Answers

**Q1: What is DNS, and why is it often called the phonebook of the Internet?**
> **Answer**: DNS stands for Domain Name System. It acts like a phonebook because humans remember friendly names (like `example.com`), but computers connect via numerical IP addresses (like `104.20.23.154`). DNS translates the name to the number.

**Q2: What is the difference between a LAN and a WAN?**
> **Answer**: A LAN (Local Area Network) covers a small, localized area like a home or school computer lab. A WAN (Wide Area Network) spans vast geographical regions, countries, or the globe; the Internet is the largest example of a WAN.

**Q3: What does the command `ping` measure?**
> **Answer**: `ping` measures network reachability and round-trip time (latency) in milliseconds by sending ICMP Echo Request packets and awaiting Echo Replies, reporting if any packets were dropped.

**Q4: What is packet switching?**
> **Answer**: Packet switching is a networking method where data is split into small chunks called packets, transmitted independently across the most efficient network routes, and reassembled at the destination.

**Q5: In client-server architecture, what role does your web browser play?**
> **Answer**: The web browser acts as the client. It formats and sends requests for web pages over the network, and then renders the server's response (HTML/CSS/JS) for the user to view.
