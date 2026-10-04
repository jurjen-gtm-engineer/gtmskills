---
name: clean-job-titles
description: Standardize verbose LinkedIn job titles into clean, usable formats
metadata:
  version: "1.0"
---

# Clean Job Titles

You are standardizing verbose or complex job titles into clean, usable formats for personalization and segmentation.

## Input

User provides:
- A raw job title (often from LinkedIn)
- Optionally: multiple titles to clean in batch

## Process

1. **Analyze Title Components**

   **Prompt Pattern:**
   ```
   For this job title:
   "[RAW TITLE]"

   Simplify to standard form by:
   1. Removing geographic qualifiers (", North America", ", EMEA")
   2. Removing company-specific branding ("Chief Evangelist & ...")
   3. Keeping the core role and seniority level
   4. Standardizing common variations
   ```

2. **Output Format**

   ```
   Original: [Verbose title]
   Cleaned: [Standardized title]

   Components:
   - Seniority: [C-level / VP / Director / Manager / IC]
   - Function: [Sales / Marketing / Engineering / etc.]
   - Specialty: [If applicable]

   Segmentation Tags:
   - seniority:[level]
   - function:[area]
   - decision_maker:[yes/no]
   ```

## Examples

**Input:** "Chief Evangelist & Head of Global Thought Leadership, North America"

**Output:**
```
Original: Chief Evangelist & Head of Global Thought Leadership, North America
Cleaned: Chief Evangelist

Components:
- Seniority: C-level equivalent
- Function: Marketing / Thought Leadership
- Specialty: Evangelism, Content

Segmentation Tags:
- seniority:executive
- function:marketing
- decision_maker:yes
```

**Input:** "Senior Director of Revenue Operations and Business Systems, Enterprise"

**Output:**
```
Original: Senior Director of Revenue Operations and Business Systems, Enterprise
Cleaned: Senior Director of Revenue Operations

Components:
- Seniority: Director
- Function: Revenue Operations
- Specialty: Business Systems

Segmentation Tags:
- seniority:director
- function:revops
- decision_maker:yes
```

**Input:** "VP, Head of Sales - SMB & Mid-Market (West Region)"

**Output:**
```
Original: VP, Head of Sales - SMB & Mid-Market (West Region)
Cleaned: VP of Sales

Components:
- Seniority: VP
- Function: Sales
- Specialty: SMB/Mid-Market

Segmentation Tags:
- seniority:vp
- function:sales
- decision_maker:yes
```

## Batch Processing

For multiple titles:

```
| Original | Cleaned | Seniority | Function |
|----------|---------|-----------|----------|
| [Title 1] | [Clean 1] | [Level] | [Area] |
| [Title 2] | [Clean 2] | [Level] | [Area] |
```

## Use Cases

1. **Email Personalization**: Use cleaned title in "Hi [Name], as a [Clean Title]..."
2. **Segmentation**: Group by seniority or function for campaigns
3. **Routing**: Route leads to appropriate sales rep by title
4. **Scoring**: Add points based on seniority level

## Related Skills

- `/role-focus` - Understand what the role focuses on
- `/ideal-customer-profiles` - Match cleaned titles to ICP

---

Examples are illustrative. Company names, prices and numbers in them are placeholders or may be out of date, so check the live source before you rely on any detail.
