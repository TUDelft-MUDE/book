module Gridap_rod
  using Gridap

  # Discrete model
  model = CartesianDiscreteModel((0.0,3.0), (10,))
  labels = get_face_labeling(model)
  add_tag_from_tags!(labels,"left",[1])
  add_tag_from_tags!(labels,"right",[2])

  # Triangulations
  Ω = Triangulation(model)
  Γ = Boundary(Ω,tags="right")

  # FE spaces
  reffe = ReferenceFE(lagrangian,Float64,1)
  V = TestFESpace(Ω,reffe,dirichlet_tags="left")
  U = TrialFESpace(V,0.0)

  # Integration measures
  dΩ = Measure(Ω,2)
  dΓ = Measure(Γ,2)

  # Problem parameters
  EA = 1.0e3
  F = 10
  q = -10

  # Weak form
  a(u,v) = ∫(EA*(∇(v)⋅∇(u)))dΩ
  l(v) = ∫(q*v)dΩ + ∫(F*v)dΓ
  op = AffineFEOperator(a,l,U,V)

  uₕ = solve(op)
  writevtk(Ω,"solution",cellfields=["u"=>uₕ])
end
