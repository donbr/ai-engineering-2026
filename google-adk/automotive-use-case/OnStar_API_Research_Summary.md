# OnStar API Research Summary: Evolution from 2012-2026

## Executive Summary

This document provides a comprehensive analysis of OnStar's API evolution, available capabilities, third-party integrations, and significant changes announced for January 2026. The research covers official GM developer resources, fleet management APIs, and consumer-facing connected vehicle services.

---

## 1. Historical Timeline of OnStar APIs

### 2012: Initial API Launch at CES

OnStar announced its first developer API initiative at CES 2012, introducing the **Advanced Telematics Operating System (ATOMS)** platform.

**Key Details:**
- Described as a "closed API" requiring developer application approval
- First partner: RelayRides (peer-to-peer car sharing service)
- Connected to 6+ million OnStar customers at launch
- Developer contact: developers@onstar.com

**Initial Capabilities:**
- Remote door unlock for car sharing
- Vehicle location access
- Basic telematics data

**Source:** [MotorTrend - 2012 CES GM OnStar API](https://www.motortrend.com/news/2012-ces-gm-onstar-open-proprietary-api-to-third-party-developers-154953/)

### 2015-2016: RemoteLink App Era

**2015 Updates:**
- RemoteLink Version 2.0 released with redesigned UI
- Background execution capability added
- Wi-Fi hotspot management for 4G LTE vehicles
- Remote start/stop included free for 5 years on 2014+ vehicles

**2016 Deprecation:**
- OnStar RemoteLink deprecated in favor of brand-specific apps
- myChevrolet, myCadillac, myBuick, myGMC apps launched
- RemoteLink functionality migrated to brand apps

**Source:** [GM Authority - OnStar RemoteLink](https://gmauthority.com/blog/gm/general-motors-technology/onstar/onstar-remotelink-app/)

### 2020: OnStar Business Solutions Launch

GM restructured fleet services, consolidating four product offerings:
1. **OnStar Safety Services**
2. **OnStar Vehicle Insights**
3. **API & Data Services**
4. **Wi-Fi Services**

**Source:** [Automotive Fleet - GM Reveals OnStar Business Solutions](https://www.automotive-fleet.com/10124458/gm-reveals-onstar-business-solutions-for-fleets)

### 2021: Network Transition & Guardian App

- TELUS partnership for 4G/5G in-vehicle mobility
- OnStar Guardian app released (June 14, 2021)
- 22 million connected vehicles globally
- ~$2B in subscription revenue projected
- September 2021: Pre-2015 vehicles notified of 2G/3G sunset

**Source:** [Wikipedia - OnStar](https://en.wikipedia.org/wiki/OnStar)

### 2024: Smart Driver Discontinuation

- OnStar Smart Driver feature discontinued (April 2024)
- Third-party telematics deals with LexisNexis and Verisk severed
- Response to customer backlash over data sharing practices
- November 2024: TOTP (Time-based One-Time Password) authentication required

**Source:** [GM-Trucks - Smart Driver Program Ends](https://www.gm-trucks.com/general-motors-ends-onstar-smart-driver-program-amid-privacy-concerns/)

---

## 2. January 2026 API Changes

### New Tiered API Plans (GM Envolve)

GM announced consolidated API service plans effective January 2026:

| Plan | Features | Target Use Case |
|------|----------|-----------------|
| **API Starter** | Engine hours, odometer, fuel level, oil life, DEF level, EV status, DTCs, lifetime energy | Basic fleet maintenance |
| **API Pro** | All Starter + Location, driver behavior (speed, braking, seatbelt), in-vehicle coaching, vehicle access commands | Fleet optimization |
| **API Elite** | All Pro + Advanced Crash Notification, Drive Block, theft alarm notifications | Security-focused fleets |

**Key Characteristics:**
- Hardware-free (no dongles required)
- Real-time data access
- GM-approved third-party provider compatible
- Built-in security features

**Source:** [GM Envolve - OnStar API Services](https://www.gmenvolve.com/software/onstar/api-services)

### FTC Settlement (January 14, 2026)

The Federal Trade Commission finalized a consent order against GM and OnStar:

**Allegations:**
- Collected and sold precise geolocation and driving behavior data without consent
- Misleading enrollment process for Smart Driver feature
- Data sold to LexisNexis and Verisk (affecting insurance rates)

**Order Requirements:**
- 5-year ban on sharing geolocation/driving data with consumer reporting agencies
- 20-year compliance period
- Affirmative consent required for each feature/service
- Data access and deletion rights for consumers
- Ability to disable geolocation collection
- Data minimization requirements
- Deletion of previously collected driver data

**Exceptions:**
- Emergency first responder data sharing permitted
- Internal research use allowed

**Source:** [FTC Press Release](https://www.ftc.gov/news-events/news/press-releases/2026/01/ftc-finalizes-order-settling-allegations-gm-onstar-collected-sold-geolocation-data-without-consumers)

---

## 3. Current API Capabilities

### Official OnStar API Data Services

| Category | Data Points |
|----------|-------------|
| **Vehicle Health** | Engine hours, odometer, oil life, fuel level, tire pressure, battery charge, DEF level, DTCs |
| **Location** | Real-time GPS, pre-delivery tracking |
| **Driver Behavior** | Speed, hard braking/acceleration, seatbelt status, coaching events |
| **EV/PHEV** | Battery level, charge state, charge notifications (start/abort/complete) |
| **Security** | Anti-theft alerts, crash notification, Drive Block |
| **Remote Commands** | Lock/unlock, horn/lights, remote start/stop, Wi-Fi management |

**Technical Implementation:**
- Apache Pulsar client for data consumption
- HTTP requests for commands
- GM Pulsar broker connection

**Source:** [flespi - OnStar GM Fleet Management API](https://flespi.com/protocols/general-motors-onstar)

### developer.gm.com Portal

The official GM Developer portal (developer.gm.com/vehicle-apis) exists but:
- Requires JavaScript to load content
- Developer access must be requested
- Contact: developer.gm.com or developers@onstar.com
- Limited public documentation available

---

## 4. Third-Party Integrations

### Smartcar API

**Overview:** Platform-agnostic API supporting 40+ vehicle brands including GM

**Capabilities:**
| Endpoint | Method | Description |
|----------|--------|-------------|
| VIN | GET | Vehicle identification number |
| Odometer | GET | Mileage reading |
| Location | GET | GPS coordinates |
| Diagnostic Codes | GET | OBD-II trouble codes |
| Battery Level | GET | EV battery status |
| Fuel Tank | GET | Fuel level |
| Lock Status | GET/POST | Door lock state and control |
| Tire Pressure | GET | TPMS readings |
| Oil Life | GET | Remaining oil life |
| Service History | GET | Maintenance records |

**Authentication:** OAuth2 flow with OnStar credentials

**Limitations:**
- Designed for non-frequent data retrieval
- 24-hour typical update frequency (without webhooks)
- Granular permissions system required

**Coverage:** North America, Europe (33 countries)

**Source:** [Smartcar - GM Integration](https://smartcar.com/brand/gm)

### Motorq

**Partnership Type:** GM-approved connected car data platform

**Capabilities:**
- Pre-delivery vehicle tracking
- Cloud-based data ingestion and normalization
- Stream analytics processing
- AI-powered insights
- In-vehicle coaching
- Fleet optimization

**Use Case Example:** COVID-19 supply chain logistics (vehicle delivery tracking)

**Source:** [Motorq-GM Partnership](https://www.nasdaq.com/press-release/gm-and-motorq-streamline-fleet-vehicle-logistics-during-covid-19-unlock-new-approach)

### Geotab Integrated Solution

**Overview:** OEM telematics integration for GM fleets

**Features:**
- API-based integration (no external hardware)
- MyGeotab platform access
- Real-time GPS, diagnostics, fuel, driver behavior
- SDK and API expandability

**Eligibility:**
- US, Canada, Mexico GM vehicles
- Most 2015+ model years
- Requires Fleet Account Number (FAN)

**Brands:** Chevrolet, Buick, GMC, Cadillac

**Source:** [Geotab GM Integration](https://www.geotab.com/gm/)

### Samsara Integration

**Launch:** June 2022

**Features:**
- Hardware-free deployment
- Real-time vehicle location, speed, fuel
- Tire pressure, seatbelt status
- Proactive maintenance alerts
- Compliance management

**Setup Requirements:**
1. Obtain Fleet Account Number (FAN) from GM
2. Purchase Samsara GM Integration Licenses
3. Activate OnStar Business Solutions app in Samsara dashboard

**Source:** [Samsara Help Center - GM Integration](https://kb.samsara.com/hc/en-us/articles/9792810797709-Integrate-with-General-Motors-OnStar-Business-Solutions)

### Other Approved Providers

- Verizon Connect
- Azuga
- Donlen
- Element Fleet
- Holman
- Wheels

---

## 5. VIN Lookup & Decoder Services

### Official Resources

| Service | URL | Features |
|---------|-----|----------|
| NHTSA VIN Decoder | vpic.nhtsa.dot.gov/decoder | Official government decoder, partial VIN support |
| DataOne Software | dataonesoftware.com | GM OEM build data, RPO codes, features |

### Third-Party Decoders

| Service | Features |
|---------|----------|
| GMPartsGiant | Free decoder, parts ordering integration |
| GMPartsDirect | VIN lookup, parts fitment |
| DecoderPO | RPO codes for Chevy, Buick, Cadillac, GMC |

### VIN Structure (2018+)

Beginning model year 2018, GM added QR codes to Certification labels containing:
- Vehicle Identification Number (VIN)
- RPO codes
- Vehicle content identification

---

## 6. Diagnostics Capabilities

### Diagnostic Trouble Codes (DTCs)

Available through OnStar API (all plans):
- High-severity DTC notifications
- Description and recommended corrective action
- Real-time alerts

### Vehicle Health Monitoring

| Data Point | Update Frequency | Plans |
|------------|------------------|-------|
| Odometer | Per ignition cycle | All |
| Tire Pressure | Real-time | All |
| Fuel Level | Per ignition cycle | All |
| Battery Charge | Real-time (EV) | All |
| Oil Life % | Per ignition cycle | All |
| Engine Hours | Per ignition cycle | All |
| DEF Level | Per ignition cycle | All |

---

## 7. Warranty & Service Scheduling

### Consumer Access

- Warranty information available via My Account on GM Support site
- Accessible through myChevrolet/myBuick/myGMC/myCadillac apps
- Preferred dealer selection for service scheduling

### Dealer Integration

- Online service scheduling through vehicle owner portal
- Diagnostic information sharing with dealers
- Maintenance history tracking

### API Access

- No public warranty lookup API documented
- Service scheduling primarily through consumer-facing apps
- Fleet customers may have dealer integration options through OnStar Business Solutions

---

## 8. Unofficial/Community APIs

### OnStarJS (Node.js)

**Repository:** github.com/samrum/OnStarJS

**Capabilities:**
- Remote start/stop
- Lock/unlock
- Diagnostics retrieval
- Location tracking

**Authentication:** Requires TOTP secret (as of November 2024)

**Warning:** Unofficial, unsanctioned - use at own risk

### GM-Vehicle-API (C#)

**Repository:** github.com/q39JzrRa/GM-Vehicle-API

**Status:** Early, unpolished, incomplete

**Warning:** Reverse-engineered, unofficial

---

## 9. Key Considerations for Development

### Authentication Changes (November 2024)

- TOTP (Time-based One-Time Password) now required
- Affects both official and unofficial API access
- Workaround requires TOTP secret for automated authentication

### Privacy Regulations Impact

Post-FTC settlement requirements:
- Explicit user consent required per feature
- Data minimization obligations
- User data access and deletion rights
- Cannot share driving data with consumer reporting agencies

### Vehicle Compatibility

| Model Year | OnStar Status |
|------------|---------------|
| Pre-2015 | Service discontinued (2G/3G sunset) |
| 2015-2024 | Supported with 4G LTE |
| 2025+ | OnStar Basics included 8 years |

---

## 10. Summary: Available APIs for Automotive Use Cases

### VIN Lookup
- **Official:** Limited (NHTSA decoder, DataOne)
- **Third-party:** Smartcar VIN endpoint, various decoder services
- **Fleet:** Available through OnStar Business Solutions

### Diagnostics
- **Official:** OnStar API (all plans) - DTCs, vehicle health
- **Third-party:** Smartcar Diagnostic Codes endpoint
- **Fleet:** Geotab, Samsara, Motorq integrations

### Warranty
- **Official:** Consumer portal only (no public API)
- **Third-party:** Not available
- **Dealer:** Internal systems only

### Service Scheduling
- **Official:** Consumer apps (myChevrolet, etc.)
- **Third-party:** Smartcar Service History endpoint (read-only)
- **Fleet:** Dealer integration through OnStar Business Solutions

---

## Sources

1. [GM Envolve - OnStar API Services](https://www.gmenvolve.com/software/onstar/api-services)
2. [Smartcar - GM Integration](https://smartcar.com/brand/gm)
3. [Smartcar API Reference](https://smartcar.com/docs/api-reference/intro)
4. [FTC Settlement Press Release](https://www.ftc.gov/news-events/news/press-releases/2026/01/ftc-finalizes-order-settling-allegations-gm-onstar-collected-sold-geolocation-data-without-consumers)
5. [MotorTrend - 2012 CES OnStar API](https://www.motortrend.com/news/2012-ces-gm-onstar-open-proprietary-api-to-third-party-developers-154953/)
6. [Geotab GM Integration](https://www.geotab.com/gm/)
7. [Samsara GM Integration](https://kb.samsara.com/hc/en-us/articles/9792810797709-Integrate-with-General-Motors-OnStar-Business-Solutions)
8. [Motorq GM Partnership](https://www.nasdaq.com/press-release/gm-and-motorq-streamline-fleet-vehicle-logistics-during-covid-19-unlock-new-approach)
9. [flespi - OnStar Protocol](https://flespi.com/protocols/general-motors-onstar)
10. [GM Authority - OnStar API](https://gmauthority.com/blog/category/onstar/onstar-api/)
11. [OnStar Wikipedia](https://en.wikipedia.org/wiki/OnStar)
12. [GM Developers Portal](https://developer.gm.com/vehicle-apis)

---

*Research compiled: January 2026*
