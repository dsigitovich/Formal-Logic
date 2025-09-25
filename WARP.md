# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository Overview

This is an educational repository teaching formal logic to programmers and AI specialists. It contains a structured 6-module curriculum spanning 12-16 weeks, with integrated progress tracking, practical exercises, and Python examples.

The repository is primarily in Russian, designed for Russian-speaking developers learning formal logic concepts.

## Common Development Commands

### Running Python Examples
```bash
# Run the main logical operators demonstration
python examples/logical-operators.py

# Run from any directory in the repository
python /Users/dmitriysigitov/Projects/Formal-Logic/examples/logical-operators.py
```

### Progress Tracking
```bash
# View learning progress (no commands needed, just open files)
# Main progress tracking file:
open progress-tracker/progress-table.md

# Usage instructions:
open progress-tracker/usage-guide.md
```

### Repository Structure Exploration
```bash
# View project structure
ls -la

# Navigate to specific sections
cd curriculum/     # Learning materials
cd exercises/      # Practical assignments  
cd examples/       # Code demonstrations
cd progress-tracker/  # Progress tracking system
cd resources/      # Additional learning resources
```

## High-Level Architecture

### Learning Path Structure
The curriculum follows a hierarchical 6-module progression:

1. **Module 1** (2-3 weeks): Logic fundamentals - concepts, statements
2. **Module 2** (3-4 weeks): Logical operations - connectives, laws
3. **Module 3** (3-4 weeks): Propositional logic - Boolean algebra, circuits  
4. **Module 4** (3-4 weeks): Predicate logic - predicates, quantifiers, inference
5. **Module 5** (2-3 weeks): Programming applications - conditional logic, algorithms
6. **Module 6** (2-3 weeks): AI applications - expert systems, modern approaches

### Progress Tracking System
The repository implements a comprehensive progress tracking system with:
- **Status indicators**: ⬜ (Not started) → 🟡 (In progress) → ✅ (Completed) → 🟢 (Verified)
- **Detailed metrics**: Module completion percentages, time tracking, test results
- **Weekly planning**: Structured learning schedules with specific topic assignments

### Code Organization
- `examples/logical-operators.py`: Comprehensive demonstration of logical operations, truth tables, De Morgan's laws, practical programming examples
- `exercises/`: Practical assignments per module (some files are placeholder/empty)
- `curriculum/`: Learning materials and detailed topic breakdowns
- Progress tracking integrated with learning materials through cross-references

## Key Learning Concepts Implemented

### Logical Operations (examples/logical-operators.py)
The main code demonstrates:
- Basic operators (AND, OR, NOT, implication, equivalence)
- Truth table construction
- Logical laws (identity, contradiction, excluded middle, De Morgan's laws)
- Advanced functions (XOR, NAND, NOR) with universality demonstrations
- Error detection using parity bits
- Practical programming examples (access control, data validation)

### Educational Approach
The repository follows **Socratic learning principles** (defined in `.cursor/rules/socratic-learning-mode.mdc`):
- Question-driven learning rather than direct answers
- 80% practical exercises, 20% explanations
- Step-by-step progression with unlocked complexity
- Real-world contextual problems
- Immediate application of theoretical concepts

## Socratic Learning Mode Integration

When working in this repository, follow the Socratic tutoring approach:
- Ask guiding questions instead of providing direct solutions
- Focus on practical exercises and code implementation
- Break complex topics into logical steps
- Frame problems in real-world programming contexts
- Encourage discovery rather than explanation

## File Dependencies

### Core Learning Files
- `curriculum/learning-path.md` → `progress-tracker/progress-table.md` (learning plan to progress tracking)
- `exercises/module-1-exercises.md` → `examples/logical-operators.py` (assignments reference code examples)
- `progress-tracker/usage-guide.md` → `progress-tracker/progress-table.md` (instructions for main tracking file)

### Python Code Structure
- `examples/logical-operators.py` is self-contained with comprehensive demonstrations
- Exercise files (`exercises/*.py`) are currently empty placeholders
- No external dependencies - uses only Python standard library

## Working with Progress Tracking

The progress tracking system is central to the learning experience:

### Status Updates
Update `progress-tracker/progress-table.md` when:
- Starting a new topic (⬜ → 🟡, add start date)
- Completing topic study (🟡 → ✅, add completion date)
- Finishing practical exercises (mark practice column)
- Completing tests (mark test column)

### Progress Calculation
- Module progress: completed topics / total topics per module
- Overall progress: completed modules / 6 total modules  
- Currently shows 25% completion (Module 2 completed, Module 1 partially done)

## Best Practices for This Repository

### When Adding New Content
- Follow the Russian language convention for documentation
- Maintain the modular structure (6 modules with 2 topics each)
- Include both theoretical explanation and practical programming examples
- Update progress tracking files when adding new exercises or topics

### When Working with Students
- Emphasize the connection between formal logic and programming concepts
- Use the existing Python examples as starting points for exploration
- Encourage regular progress tracking to maintain motivation
- Point to `resources/recommended-books.md` for additional learning materials

### Code Development
- Keep Python examples practical and related to programming/AI concepts
- Demonstrate logical concepts through executable code
- Include comprehensive docstrings and comments
- Show both theoretical foundations and real-world applications

The repository serves as both a learning platform and a practical toolkit for understanding how formal logic applies to programming and artificial intelligence development.
